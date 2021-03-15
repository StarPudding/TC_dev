import sys

from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from openpyxl import load_workbook
from all_test.src.user.safe.authentication import check
from all_test.main.run_test import RunTest
import simplejson as json


# 上传文件，为之后的测试做准备
@require_http_methods(["POST"])
@check()
def UploadFile(request):
    test_file = request.FILES.get('test_file')
    json_file = request.FILES.get('json_file')
    with open('all_test/test_file/'+test_file.name, 'wb+') as f:
        for chunk in test_file.chunks():
            f.write(chunk)
        print(test_file)
        f.close()
    with open('all_test/json_file/'+json_file.name, 'wb+') as f:
        for chunk in json_file.chunks():
            f.write(chunk)
        f.close()
    # 生成输出文件
    data = load_workbook('all_test/test_file/'+test_file.name)
    data.copy_worksheet(data.worksheets[0])
    data.save('all_test/test_file/' + test_file.name.split('.')[0]+'_out.xlsx')

    file_name = {'test_file': str(test_file.name), 'json_file': str(json_file.name)}

    response = {'code': 200, 'message': "文件上传成功", 'data': file_name}

    return JsonResponse(response)


@require_http_methods(["POST"])
def TestOne(request):
    req = json.loads(request.body)
    row = req['row']
    test_file_name = req['testFileName']
    json_file_name = req['jsonFileName']
    cookie = req['cookie']
    print(cookie)
    run_test = RunTest(cookie=cookie, data_file_name=test_file_name, json_file_name=json_file_name)
    result = run_test.run_it_by_row_num(int(row))
    print(result)
    response = {'code': 200, 'message': "执行完毕", 'data': result}

    return JsonResponse(response)


@require_http_methods(["POST"])
def AddTestCase(request):
    req = json.loads(request.body)
