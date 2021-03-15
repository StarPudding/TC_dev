from django.http import JsonResponse

from all_test.util.operation_token import Token


def check():
    def wrapper(func):
        def inner(request):
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                response = {'code': 401, 'message': "用户信息失效，请重新登录", 'data': ''}
                return JsonResponse(response)
            mess = Token.check_token(token)
            if mess == '0':
                response = {'code': 401, 'message': "用户信息失效，请重新登录", 'data': ''}
                return JsonResponse(response)
            elif mess == '1':
                response = {'code': 401, 'message': "用户名或密码错误，请重试", 'data': ''}
                return JsonResponse(response)
            else:
                out = func(request)
                return out
        return inner

    return wrapper
