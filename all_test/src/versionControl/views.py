from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import simplejson as json
import re
from all_test.src.system.mapping import project_environment
from all_test.util.operation_jenkins import OperationJenkins
from all_test.util.operation_winrm import OperationWINRM
from all_test.data.system_data import SystemData
from all_test.src.user.safe.authentication import check
from all_test.util.CommonUtil import CommonUtil
from all_test.src.versionControl.mapping import version


def getSVNInfo(project_id, environment_id):
    out = project_environment.getSVNInfo(project_id=project_id, environment_id=environment_id)[0]
    return out


# 获得正确的merge指令
def getRightCommend(list, svn_info):
    # 连接远程cmd
    sd = SystemData()
    ip = sd.getRemoteIp()  # ip
    username = sd.getRemoteUsername()  # 用户名
    password = sd.getRemotePassword()  # 密码
    rm = OperationWINRM(ip, username, password)
    out = rm.do_cmd("svn log -q -r " + list[0] + ":" + list[len(list)-1] + " \"" + svn_info.svn_position + "\""
                    + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password + " --no-auth-cache"
                    + " | findstr \"r.*\"")

    out = re.findall("(?<=r)[0-9]*?(?=\\s)", out)
    print(out)

    cmd = ''
    begin = 0
    cur = 1
    while cur < len(list):
        flag = isCoherent(list[begin], list[cur], cur - begin + 1, out)
        print(flag)
        if flag == 1:
            if cur == len(list) - 1:
                cmd = cmd + '-r ' + str(int(list[begin])-1) + ":" + str(list[cur]) + ' '
                cur = cur + 1
            else:
                cur = cur + 1
            continue
        elif flag == 0:
            if begin == cur - 1:
                cmd = cmd + '-c ' + str(list[begin]) + ' '
            else:
                cmd = cmd + '-r ' + str(int(list[begin])-1) + ":" + str(list[cur - 1]) + ' '
            # 如果检查完毕，则将最后一个加上去
            if cur == len(list) - 1:
                cmd = cmd + "-c " + str(list[cur])
                cur = cur + 1
            # 否则，将从此开始，进行下一轮
            else:
                begin = cur
                cur = cur + 1

        else:
            cmd = ''
            break
    # 如果cur依然为1，说明只有一个版本
    if cur==1:
        cmd = cmd + "-c " + list[0]
    return cmd


def isCoherent(begin_vision, end_vision, differ, all):
    print(begin_vision, end_vision)

    begin, end = 0, 0
    for i in range(0, len(all)):
        if all[i] == begin_vision:
            begin = i
            break
        elif i == len(all) - 1:
            return 2

    for i in range(0, len(all)):
        if all[i] == end_vision:
            end = i
            break
        elif i == len(all) - 1:
            return 2

    result = end - begin + 1

    if differ == result:
        return 1
    else:
        return 0


# 更新版本
@require_http_methods(["POST"])
@check()
def UpdateVersion(request):
    req = json.loads(request.body)
    project_id = req['project_id']
    environment_id = req['environment_id']
    # 获得远程服务器信息
    sd = SystemData()
    ip = sd.getRemoteIp()  # ip
    username = sd.getRemoteUsername()  # 用户名
    password = sd.getRemotePassword()  # 密码
    # 连接远程cmd
    rm = OperationWINRM(ip, username, password)
    # 获得svn相关信息
    svn_info = getSVNInfo(project_id=project_id, environment_id=environment_id)
    # 执行更新命令
    data = rm.do_cmd("svn update --ignore-externals " + "\"" + svn_info.project_position + "\""
                     + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
                     + " --no-auth-cache")
    cm = CommonUtil()
    if cm.is_contain("At revision", data):
        response = {'code': 200, 'message': "success", 'data': data}
    else:
        response = {'code': 200, 'message': "fail", 'data': data}
    return JsonResponse(response)


# 合并版本
@require_http_methods(["POST"])
@check()
def CombineVersion(request):
    req = json.loads(request.body)
    sd = SystemData()
    version_list = req['versionList']
    version_list = str(version_list)
    version_list = version_list.split(',')

    ip = sd.getRemoteIp()  # ip
    username = sd.getRemoteUsername()  # 用户名
    password = sd.getRemotePassword()  # 密码
    rm = OperationWINRM(ip, username, password)

    project_id = req['project_id']
    environment_id = req['environment_id']

    svn_info = getSVNInfo(project_id=project_id, environment_id=environment_id)

    cmd = getRightCommend(version_list, svn_info)
    # list_command = ""
    # for i in version_list:
    #     list_command = list_command + " -c " + i
    if environment_id != '3':
        print("svn merge " + svn_info.svn_position + " " + cmd + " "
              + "\"" + svn_info.project_position + "\""
              + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
              + " --no-auth-cache")

        data = rm.do_cmd("svn merge " + svn_info.svn_position + " " + cmd + " "
                         + "\"" + svn_info.project_position + "\""
                         + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
                         + " --no-auth-cache --non-interactive")
    else:
        print("svn merge " + svn_info.svn_position + " " + cmd + " "
              + "\"" + svn_info.project_position + "\""
              + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
              + " --no-auth-cache")

        data = rm.do_cmd("svn merge " + svn_info.svn_position + " " + cmd + " "
                         + "\"" + svn_info.project_position + "\""
                         + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
                         + " --no-auth-cache --non-interactive")

    cm = CommonUtil()
    if cm.is_contain("Summary of conflicts", data):
        conflicts = re.findall("C .*?\n", data)
        conflicts_str = ''
        for conflict in conflicts:
            conflicts_str = conflicts_str + str(conflict)
        data = str(data) + '\n 冲突如下：\n' + conflicts_str
        response = {'code': 200, 'message': "conflicts", 'data': data}
    else:
        response = {'code': 200, 'message': "success", 'data': data}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def CommitVersion(request):
    req = json.loads(request.body)
    sd = SystemData()
    # sd = SystemData('TSY_TEST')
    ip = sd.getRemoteIp()  # ip
    username = sd.getRemoteUsername()  # 用户名
    password = sd.getRemotePassword()  # 密码
    rm = OperationWINRM(ip, username, password)
    message = req['message']

    project_id = req['project_id']
    environment_id = req['environment_id']
    svn_info = getSVNInfo(project_id=project_id, environment_id=environment_id)
    data = rm.do_cmd(" svn commit -m " + message + " "
                     + "\"" + svn_info.project_position + "\""
                     + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
                     + " --no-auth-cache")
    response = {'code': 200, 'message': "执行完毕", 'data': data}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def RevertVersion(request):
    req = json.loads(request.body)
    sd = SystemData()
    ip = sd.getRemoteIp()  # ip
    username = sd.getRemoteUsername()  # 用户名
    password = sd.getRemotePassword()  # 密码
    rm = OperationWINRM(ip, username, password)
    project_id = req['project_id']
    environment_id = req['environment_id']
    svn_info = getSVNInfo(project_id=project_id, environment_id=environment_id)

    data = rm.do_cmd("svn revert -R " + "\"" + svn_info.project_position + "\""
                     + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
                     + " --no-auth-cache")
    response = {'code': 200, 'message': "执行完毕", 'data': data}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def CleanupVersion(request):
    req = json.loads(request.body)
    sd = SystemData()
    ip = sd.getRemoteIp()  # ip
    username = sd.getRemoteUsername()  # 用户名
    password = sd.getRemotePassword()  # 密码
    rm = OperationWINRM(ip, username, password)

    project_id = req['project_id']
    environment_id = req['environment_id']
    svn_info = getSVNInfo(project_id=project_id, environment_id=environment_id)

    data = rm.do_cmd("svn cleanup " + "\"" + svn_info.project_position + "\"")
    response = {'code': 200, 'message': "执行完毕", 'data': data}
    return JsonResponse(response)


# 展示日志
@require_http_methods(["POST"])
@check()
def ListLog(request):
    req = json.loads(request.body)
    sd = SystemData()
    ip = sd.getRemoteIp()  # ip
    username = sd.getRemoteUsername()  # 用户名
    password = sd.getRemotePassword()  # 密码
    rm = OperationWINRM(ip, username, password)
    project_id = req['project_id']
    environment_id = req['environment_id']
    number = req['number']
    svn_info = getSVNInfo(project_id=project_id, environment_id=environment_id)

    data = rm.do_cmd("svn log " + "\"" + svn_info.project_position + "\"" + " -l " + str(number)
                     + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
                     + " --no-auth-cache")
    print(data)
    # 基础信息
    base_str = re.findall("r.*?1 line", data)
    # 备注信息
    remark_str = re.findall(r"(?<=1 line\r\n)([\s\S]+?)(?=\n-------------------)", data, re.M)
    dataset = []
    count = 0
    print(len(base_str))
    print(len(remark_str))
    for base in base_str:
        base_info = base.split(' | ')
        remark = remark_str[count]
        count = count + 1
        data = {
            'version': base_info[0],
            'author': base_info[1],
            'date': base_info[2],
            'remark': remark
        }
        dataset.append(data)
    response = {'code': 200, 'message': "执行完毕", 'data': dataset}
    return JsonResponse(response)


# jenkins构建
@require_http_methods(["POST"])
@check()
def JenkinsBuild(request):
    req = json.loads(request.body)
    project_id = req['project_id']
    environment_id = req['environment_id']
    svn_info = getSVNInfo(project_id=project_id, environment_id=environment_id)

    oj = OperationJenkins(url=svn_info.jenkins_url, username=svn_info.jenkins_username,
                          password=svn_info.jenkins_password)
    oj.do_job(job_name=svn_info.jenkins_job)
    response = {'code': 200, 'message': "正在构建中", 'data': ''}
    return JsonResponse(response)


# 获得所有的项目
# jenkins构建
@require_http_methods(["POST"])
@check()
def getAllProjects(request):
    result = version.getAllProjects()

    dataset = []

    for item in result:
        print(item.CodeValue)
        dataset.append(item.CodeValue)

    response = {'code': 200, 'message': '获得项目成功', 'data': dataset}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def getSVNVersionList(request):
    req = json.loads(request.body)
    project_id = req['project_id']
    environment_id = req['environment_id']
    # 获得远程服务器信息
    sd = SystemData()
    ip = sd.getRemoteIp()  # ip
    username = sd.getRemoteUsername()  # 用户名
    password = sd.getRemotePassword()  # 密码
    # 连接远程cmd
    rm = OperationWINRM(ip, username, password)
    # 获得svn相关信息
    svn_info = getSVNInfo(project_id=project_id, environment_id=environment_id)
    # 执行log命令
    data = rm.do_cmd("svn log " + "\"" + svn_info.svn_position + "\"" + " -l " + '100'
                     + " --username " + svn_info.svn_username + " --password " + svn_info.svn_password
                     + " --no-auth-cache")

    print(data)
    # 基础信息
    base_str = re.findall("r.*?1 line", data)
    # 备注信息
    remark_str = re.findall(r"(?<=1 line\r\n)([\s\S]+?)(?=\n-------------------)", data, re.M)
    dataset = []
    count = 0
    print(len(base_str))
    print(len(remark_str))
    for base in base_str:
        base_info = base.split(' | ')
        remark = remark_str[count]
        count = count + 1
        data = {
            'version': base_info[0][1:],
            'author': base_info[1],
            'date': base_info[2],
            'remark': remark
        }
        dataset.append(data)
    response = {'code': 200, 'message': "执行完毕", 'data': dataset}
    return JsonResponse(response)
