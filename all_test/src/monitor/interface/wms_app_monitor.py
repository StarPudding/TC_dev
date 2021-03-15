import sys

from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from all_test.main.run_test import RunTest
import simplejson as json
from ..mapping import monitor
from all_test.base.run_method import RunMethod
from all_test.util.CommonUtil import CommonUtil
from all_test.src.user.safe.authentication import check

from all_test.cronjobs import timer


# 登录wms app端并登录监控
@require_http_methods(["POST"])
def login(request):
    rm = RunMethod()
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
        "username":	"dsadmin",
        "password":	"aff8c7c4f8d9fab3bb7322ea79cc5170",
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
    # 填充返回结果
    data = {
        'wms_cookie': wms_cookie,
        '8700_cookie': cookie
    }
    print("-------------------登录成功------------------")
    response = {'code': 200, 'message': '登陆成功', 'data': data}
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


# 取得所有仓库
@require_http_methods(["POST"])
@check()
def get_all_warehouse(request):
    # req = json.loads(request.body)
    # cookie = req['wms_cookie']
    # print(cookie)
    # url = "http://wms.zmd.com.cn//api/camera/warehousePartition/list"
    # data = {
    # }
    # # 请求头
    # header = {
    #     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    # }
    # rm = RunMethod()
    # print(url, data, header, cookie)
    # req = rm.post_main(url=url, data=data, header=header, cookies=cookie)
    # print(req.json())
    #
    # response = {'code': 200, 'message': '已获得所有仓库', 'data': req.json()}

    # monitor.monitor()
    response = {'code': 200, 'message': '已获得所有仓库', 'data': ''}
    return JsonResponse(response)


# 取得选择仓库所有监控的信息
@require_http_methods(["POST"])
def show_monitor_info(request):
    # req = json.loads(request.body)
    # run_test = RunTest(req['cookie'])
    # num = run_test.get_test_num()
    #
    # monitors = []
    # for i in range(4, num+1):
    #     monitor = {}
    #     name, last_update_time, error_count, status = run_test.run_it_by_row_num(i)
    #     monitor['name'] = name
    #     monitor['last_fail_time'] = last_update_time
    #     monitor['fail_count'] = error_count
    #     if status == 'pass':
    #         status = "正常"
    #     else:
    #         status = "故障"
    #     monitor['status'] = status
    #     monitors.append(monitor)
    req = json.loads(request.body)
    warehouse_name = req['warehouse_name']
    datas = monitor.getAllMonitor(warehouse_name=warehouse_name)
    for data in datas:
        data['status'] = '未开始'
    response = {'code': 200, 'message': '已获得监控状态', 'data': datas}
    return JsonResponse(response)


# 取得单个监控的状态
@check()
@require_http_methods(["POST"])
def get_monitor_status(request):
    req = json.loads(request.body)
    monitor_id = req['monitor_id']
    cookie = req['cookie']
    result = monitor.getMonitorById(monitor_id=monitor_id)
    url = result['monitor_url']

    print(result)
    sys_code = result['sysCode']
    data = {
        "sessionID": "01D9A743AF3DDF5D7CBD7B36CC2405E8",
        "cameraID": "",
        "sysCode": sys_code
    }
    # 请求头
    header = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    rm = RunMethod()
    cm = CommonUtil()
    print(url, data, header, cookie)
    req = rm.post_main(url=url, data=data, header=header, cookies=cookie)
    status = ''
    if cm.is_contain('<IsOnline>1</IsOnline>', req.text):
        status = "在线"
    else:
        status = "不在线"
    response = {'code': 200, 'message': '已获得监控状态', 'data': status}
    return JsonResponse(response)