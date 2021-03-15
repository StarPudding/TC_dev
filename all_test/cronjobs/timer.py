import atexit
import fcntl
import time
import urllib3

from all_test.base.run_method import RunMethod
from all_test.util.CommonUtil import CommonUtil
from all_test.util.send_email import SendEmail
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from all_test.src.monitor.mapping import warehouse_monitor

# 实例化调度器
scheduler = BackgroundScheduler()
# 调度器使用默认的DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), 'default')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 每天整点或者半点时执行任务
@register_job(scheduler, 'cron', id='monitor',  minute='0', replace_existing=True)
def monitor():
    # 第一步，登录wms
    rm = RunMethod()
    cm = CommonUtil()
    # 登录wms参数

    wms_login = {
        "userName": "唐顺意",
        "password": "Tsy@123456",
        "pushClientId": "null",
        "deviceId": "",
        "deviceType": "app",
        "phoneType": "EVR-AL00",
        "loginFrom": "Android",
        "appVersion": "1.1.6"
    }
    # 登录wms url
    wms_login_url = "http://wms.zmd.com.cn//api/login"
    # 登录监控平台参数
    monitor_login = {
        "username": "dsadmin",
        "password": "aff8c7c4f8d9fab3bb7322ea79cc5170",
        "mac": "02:00:00:00:00:00",
        "loginAddr": "115.238.88.202",
        "passwordLevel": "2",
        "captchaKey": "",
        "captcha": ""
    }
    # 登录监控平台url
    monitor_login_url = "https://115.238.88.202:1443/msp/mobile/login"
    # 请求头
    header = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    rm.post_main(url=wms_login_url, data=wms_login, header=header)
    wms_cookie = rm.getCookies(url=wms_login_url, data=wms_login, header=header)
    rm.post_main(url=monitor_login_url, data=monitor_login, header=header, cookies=wms_cookie)
    cookie = rm.getCookies(url=monitor_login_url, data=monitor_login, header=header)

    # 第二步，取得所有仓库的信息
    url = "http://wms.zmd.com.cn//api/camera/warehousePartition/list"
    data = {
    }
    # 请求头
    header = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    rm = RunMethod()
    print(url, data, header, wms_cookie)
    req = rm.post_main(url=url, data=data, header=header, cookies=wms_cookie)
    warehouses = req.json()

    warehouse_infos = []
    cur = 0
    # 第三步，检查仓库下面的监控列表
    warehouse_monitor.initStatus()
    for warehouse in warehouses:
        # cur = cur + 1
        # if cur > 4:
        #     break
        online_list = []
        offline_list = []
        warehouse_url = "http://wms.zmd.com.cn//api/camera/userCamera/list"
        warehouse_data = {
            'warehouseId': warehouse['id'],
            'partitionId': ''
        }
        # 请求头
        warehouse_header = {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        }
        rm = RunMethod()
        req = rm.post_main(url=warehouse_url, data=warehouse_data, header=warehouse_header, cookies=wms_cookie)

        # 监控列表
        monitors = req.json()

        for item in monitors:
            if type(item) == str:
                print(item)
                print(item['cameraName'] + ' ' + warehouse['warehouseName'] + '   异常')
                offline_list.append(item['cameraName'])
                break
            url_8700 = "https://115.238.88.202:1443/msp/mobile/getCameraInfo"
            data_8700 = {
                "sessionID": "01D9A743AF3DDF5D7CBD7B36CC2405E8",
                "cameraID": "",
                "sysCode": item['cameraUuid']
            }
            # 请求头
            header_8700 = {
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            }
            req = rm.post_main(url=url_8700, data=data_8700, header=header_8700, cookies=cookie)
            if cm.is_contain('<IsOnline>1</IsOnline>', req.text):
                online_list.append(item['cameraName'])
            else:
                offline_list.append(item['cameraName'])
        is_normal = True
        if len(offline_list) != 0:
            is_normal = False
        warehouse_info = {
            'warehouseName': warehouse['warehouseName'],
            'online': online_list,
            'offline': offline_list,
            'is_normal': is_normal,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # time.strftime("%H:%M:%S", time.localtime()
        }
        warehouse_infos.append(warehouse_info)

    # 第四步，邮件通知
    content = "此次一共检查仓库个数为%s个," % len(warehouse_infos)
    wrong_count = 0
    wrong_content = ""
    for item in warehouse_infos:
        # 判断之前是否有过这个仓库
        flag = warehouse_monitor.getMessage(item['warehouseName'])
        is_normal = item['is_normal']

        # 取得所有数据
        online_count = len(item['online'])
        offline_count = len(item['offline'])
        offline_list_str = ''
        for offline in item['offline']:
            offline_list_str = offline_list_str + offline + ','
        # 如果监控正常
        if is_normal:
            # 且没有这个仓库，则在表中新增
            if flag is None:
                warehouse_monitor.addMessage(warehouse_name=item['warehouseName'],
                                             online=len(item['online']),
                                             offline=len(item['offline']),
                                             offline_list=offline_list_str,
                                             check_time=item['time'])
            # 且有这个仓库，则比较与上次的差别，并且更新表
            else:
                last = warehouse_monitor.getMessage(warehouse_name=item['warehouseName'])
                # 如果比历史最大在线数小
                if last.max_online>online_count:
                    # 记录
                    wrong_content = wrong_content + "【" + item['warehouseName'] + "】" + "【检测时间: " + item['time'] + "】" \
                                    '当前监控在线数(%s)小于历史最大在线数(%s), 请核查!\r\n'\
                                    % (online_count, last.max_online)
                    wrong_count = wrong_count + 1
                warehouse_monitor.addMessage(warehouse_name=item['warehouseName'],
                                             online=online_count,
                                             offline=offline_count,
                                             offline_list=offline_list_str,
                                             check_time=item['time'])

        # 监控不正常
        else:
            wrong_content = wrong_content + "【" + item['warehouseName'] + "】" + "【检测时间: " + item['time'] + "】" \
                            "有%s个异常监控：\r\n" % len(item['offline'])
            for wrong in item['offline']:
                wrong_content = wrong_content + str(wrong) + '\r\n'
            wrong_count = wrong_count + 1
            warehouse_monitor.addMessage(warehouse_name=item['warehouseName'],
                                         online=online_count,
                                         offline=offline_count,
                                         offline_list=offline_list_str,
                                         check_time=item['time'])

    if wrong_count > 0:
        content = content + "其中有%s个仓库存在异常监控，如下：\r\n" % wrong_count
        content = content + wrong_content
        user_list = ['tangsy2@zmd.com.cn']
        sub = "%s个仓库在线" % len(warehouse_infos) + ", %s个仓库异常" % wrong_count

    else:
        sub = "%s个仓库在线" % len(warehouse_infos)
        user_list = ['tangsy2@zmd.com.cn']
        content = "监控正常 \r\n"

    not_check = warehouse_monitor.getNotCheckWarehouseName()
    not_check_str = ''
    for item in not_check:
        not_check_str = not_check_str + '【' + item + '】'
        warehouse_monitor.updateCheckTime(item)
    if len(not_check) != 0:
        sub = sub + ", %s个仓库掉线" % len(not_check)
        content = content + not_check_str + '未被检查，可能掉线，请核实!'
    em = SendEmail()
    em.send_mail(user_list, sub, content)


# 添加任务
def add_job(job_id, func, args, type, job_time):

    scheduler.add_job(id=job_id, func=func, args=args, trigger=type)


scheduler.start()
