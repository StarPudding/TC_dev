from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import simplejson as json
from ..mapping import user
from all_test.util.operation_token import Token


# 登录
@require_http_methods(["POST"])
def login(request):
    req = json.loads(request.body)
    username = req['username']
    password = req['password']
    token_data = {'username': username, 'password': password}
    response = {'code': 200, 'message': "登录成功", 'data': None}
    token = Token.create_token(token_data)
    data = {'token': token}
    if user.isUserExists(username, password):
        response['message'] = "登录成功"
    else:
        response['message'] = "登录失败"
        response['code'] = 401
    response['data'] = data
    return JsonResponse(response)

