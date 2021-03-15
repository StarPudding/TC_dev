from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from all_test.src.user.safe.authentication import check
import json
from all_test.src.monitor.mapping import warehouse_monitor


@require_http_methods(["POST"])
@check()
def getMonitorInfo(request):
    req = json.loads(request.body)
    status = req['status']
    name = req['name']
    if name == '':
        name = None
    out = warehouse_monitor.getMessage(warehouse_name=name, status=status)

    dataset = []
    for item in out:
        data = {
            'name': item.warehouse_name,
            'max_online': item.max_online,
            'last_online': item.last_online,
            'last_check_time': str(item.last_check_time)
        }
        if item.last_check_time is None:
            data['last_check_time'] = '-'
            data['status'] = '未被检查'
        else:
            if item.max_online != item.last_online:
                data['status'] = '异常'
            else:
                data['status'] = '正常'
        dataset.append(data)
    print(dataset)
    response = {'code': 200, 'message': "获得仓库信息列表成功", 'data': dataset}
    return JsonResponse(response)


@require_http_methods(["POST"])
@check()
def getAllWarehouse(request):

    out = warehouse_monitor.getAllWarehouseName()
    dataset = []
    for item in out:
        data = {
            'name': item.warehouse_name,
        }
        dataset.append(data)
    print(dataset)
    response = {'code': 200, 'message': "获得仓库列表成功", 'data': dataset}
    return JsonResponse(response)



