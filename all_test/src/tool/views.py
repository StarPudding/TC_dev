from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import simplejson as json
from all_test.src.user.safe.authentication import check
from all_test.tools import tools


@require_http_methods(["POST"])
@check()
def CombineSQLAndParameter(request):
    req = json.loads(request.body)
    sql = req['sql']
    parameter = req['parameter']
    result = tools.CombineSQLAndParameter(sql, parameter)
    print(result)
    response = {'code': 200, 'message': "成功", 'data': result}
    return JsonResponse(response)
