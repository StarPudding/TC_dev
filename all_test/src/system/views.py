from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from all_test.src.user.safe.authentication import check
import json
from all_test.src.system.mapping import project, menu, environment, project_environment, user


@require_http_methods(["POST"])
@check()
def getMenu(request):
    # req = json.loads(request.body)
    # username = req['username']
    # password = req['password']
    results = menu.getAllRootMenu()
    dataset = []
    for result in results:
        data = {
            'id': result.menu_id,
            'name': result.menu_name,
            'url': result.menu_url,
            'parent_id': result.parent_id,
            'has_child': True,
            'sort': result.sort_id,
            'is_show': result.is_show,
            'authority': result.authority,
            'menu_icon': result.menu_icon
        }
        dataset.append(data)
    print(dataset)
    response = {'code': 200, 'message': "获得根目录成功", 'data': dataset}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def getChildMenu(request):
    req = json.loads(request.body)
    parent_id = req['id']
    childes = menu.getChild(parent_id=parent_id)
    dataset = []
    for result in childes:
        data = {
            'id': result.menu_id,
            'name': result.menu_name,
            'url': result.menu_url,
            'parent_id': result.parent_id,
            'has_child': True,
            'sort': result.sort_id,
            'is_show': result.is_show,
            'authority': result.authority,
            'menu_icon': result.menu_icon,
        }
        dataset.append(data)
    response = {'code': 200, 'message': "获得根目录成功", 'data': dataset}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def addChildMenu(request):
    req = json.loads(request.body)
    menu_info = req['menu_info']
    data = {
        'menu_name': menu_info['name'],
        'menu_url': menu_info['url'],
        'parent_id': menu_info['parent_id'],
        'sort_id': menu_info['sort'],
        'is_show': menu_info['is_show'],
        'authority': menu_info['authority'],
        'menu_icon': menu_info['menu_icon'],
    }
    menu.addMenu(menu_info=data)
    response = {'code': 200, 'message': "添加子菜单成功", 'data': ''}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def updateMenu(request):
    req = json.loads(request.body)
    menu_info = req['menu_info']
    data = {
        'menu_id': menu_info['id'],
        'menu_name': menu_info['name'],
        'menu_url': menu_info['url'],
        'parent_id': menu_info['parent_id'],
        'sort_id': menu_info['sort'],
        'is_show': menu_info['is_show'],
        'authority': menu_info['authority'],
        'menu_icon': menu_info['menu_icon'],
    }
    menu.updateMenu(data)
    response = {'code': 200, 'message': "更新菜单成功", 'data': ''}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def deleteMenu(request):
    req = json.loads(request.body)
    menu_id = req['menu_id']
    menu.deleteMenu(menu_id=menu_id)
    response = {'code': 200, 'message': "删除菜单成功", 'data': ''}
    return JsonResponse(response)


@require_http_methods(["POST"])
def getAllMenu(request):
    req = json.loads(request.body)
    all_root_menu = menu.getAllRootMenu()
    dataset = []
    count = 1
    for root_menu in all_root_menu:
        id = root_menu.menu_id
        childes = menu.getChild(id)
        child_data = []
        for child in childes:
            data = {
                'menu_id': child.menu_id,
                'menu_name': child.menu_name,
                'menu_url': child.menu_url,
                'parent_id': child.parent_id,
                'is_show': child.is_show,
                'authority': child.authority,
                'menu_icon': child.menu_icon,
            }
            child_data.append(data)
        data = {
            'menu_id': root_menu.menu_id,
            'menu_name': root_menu.menu_name,
            'parent_id': root_menu.parent_id,
            'is_show': root_menu.is_show,
            'authority': root_menu.authority,
            'menu_icon': root_menu.menu_icon,
            'child': child_data,
            'index': count
        }
        count = count + 1
        dataset.append(data)
    response = {'code': 200, 'message': "获得菜单成功", 'data': dataset}
    return JsonResponse(response)


# 获得所有项目
@require_http_methods(["POST"])
@check()
def getAllProject(request):
    projects = project.getAllProject()
    dataset = []
    for item in projects:
        data = {
            'project_id': item.project_id,
            'project_name': item.project_name
        }
        dataset.append(data)
    response = {'code': 200, 'message': "获得项目列表成功", 'data': dataset}
    return JsonResponse(response)


# 获得所有环境
@require_http_methods(["POST"])
@check()
def getEnvironmentOfProject(request):
    req = json.loads(request.body)
    project_id = req['project_id']
    print("----------------------------------------------------")
    environments = environment.getAllEnvironmentOfProject(project_id=project_id)
    dataset = []
    for item in environments:
        data = {
            'environment_id': item.environment_id,
            'environment_name': item.environment_name
        }
        dataset.append(data)
    response = {'code': 200, 'message': "获得环境列表成功", 'data': dataset}
    return JsonResponse(response)


# 获得所有项目和环境
@require_http_methods(["POST"])
@check()
def getAllProjectAndEnvironment(request):
    req = json.loads(request.body)
    project_id = req['project_id']
    environment_id = req['environment_id']
    results = project_environment.getAllMainInfo(project_id=project_id, environment_id=environment_id)
    dataset = []
    for item in results:
        data = {
            'id': item.id,
            'environment_id': item.environment_id,
            'environment_name': item.environment_name,
            'project_id': item.project_id,
            'project_name': item.project_name
        }
        dataset.append(data)
    response = {'code': 200, 'message': "获得环境列表成功", 'data': dataset}
    return JsonResponse(response)


# 查看项目、环境基本信息
@require_http_methods(["POST"])
@check()
def getMainInfo(request):
    req = json.loads(request.body)
    id = req['id']
    result = project_environment.getMainInfo(id=id)[0]
    dataset = []

    data = {
            'project_position': result.project_position,
            'svn_position': result.svn_position,
            'jenkins_position': result.jenkins_url + ": " + result.jenkins_job,
        }
    dataset.append(data)
    response = {'code': 200, 'message': "获得项目基本信息成功", 'data': data}
    return JsonResponse(response)


# 获得用户列表的接口
@require_http_methods(["POST"])
@check()
def getUser(request):
    req = json.loads(request.body)
    print(req)
    current_page = req['current_page']
    page_size = req['page_size']
    users, count = user.getAllUser(current_page=current_page, page_size=page_size)
    dataset = []
    for item in users:
        data = {
            'id': item.id,
            'username': item.username,
            'mobile': item.mobile,
            'email': item.email
        }
        dataset.append(data)
    return_data = {'dataset': dataset, 'count': count}
    response = {'code': 200, 'message': "获得用户列表成功", 'data': return_data}
    return JsonResponse(response)


# 新增用户的接口
@require_http_methods(["POST"])
@check()
def addUser(request):
    pass