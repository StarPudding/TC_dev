# coding:utf-8
import http
import re
from http import cookiejar
from urllib import request

from all_test.base.run_method import RunMethod
from all_test.data.dependent_data import DependentData
from all_test.data.get_data import GetData
from all_test.util.CommonUtil import CommonUtil
from all_test.util.operation_json import OperationJson
from all_test.util.operation_html import OperationHtml
from all_test.util.send_email import SendEmail
import requests
global COOKIES


def getCookies(method, url, data, header):
    session = requests.Session()
    if method == 'post':
        session.post(url, data, headers=header, verify=False)
    print("cookies:" + str(session.cookies.get_dict()))
    return session.cookies.get_dict()


class RunTest:
    def __init__(self, cookie=None, data_file_name=None, json_file_name=None):
        self.run_method = RunMethod()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()
        self.cookie = cookie
        self.pass_count = []
        self.fail_count = []
        # json文件
        self.json_file_name = 'all_test/json_file/' + json_file_name
        self.json = OperationJson(self.json_file_name)

        # case文件
        self.data_file_name = 'all_test/test_file/' + data_file_name
        # result文件
        self.result_file_name = 'all_test/test_file/' + data_file_name.split('.')[0]+'_out.xlsx'
        # 获得需要提取数据的excel
        self.data = GetData(file_name=self.data_file_name, sheet_id=0)
        # 获取需要写入的excel
        self.result_data = GetData(file_name=self.result_file_name, sheet_id=0)

    # 根据行号运行
    def run_it_by_row_num(self, row):
        # 返回的结果
        result = {'cookie': ''}

        case_id = self.data.get_case_id(row)
        url = self.data.get_request_url(row)
        method = self.data.get_request_method(row)

        header = self.data.is_header(row)
        is_cookie = self.data.is_cookie(row)
        expect = self.data.get_expect_data(row)

        # case是否有依赖case
        dependent_case = self.data.get_depend_case(row)
        # case是否有依赖数据
        dependent_data = self.data.get_depend_key(row)
        # case得到依赖数据应该填在哪
        target_data = self.data.get_depend_field(row)
        # case得到依赖数据之后应该填在json的哪个大类中
        request_data = self.data.get_request_data(row)
        # case得到的数据是什么类型的

        if dependent_case is not None:
            # 有case依赖，首先运行case依赖的case
            # 先通过依赖case_id获得相应行号
            row_num = self.result_data.opera_excel.get_row_num(dependent_case)

            # 取得对应行号的是否成功与返回数据

            # 判断时，应取最新的excel数据
            new_data = GetData(self.result_file_name, sheet_id=0)
            is_pass = new_data.get_isPass(row_num)
            response_data = new_data.get_result(row_num)

            # 获取返回结果的类型
            response_type = new_data.get_response_type(row_num)
            print("pass: ", is_pass)
            if is_pass is not None and response_data is not None:
                # 如果两者非空,则不需要执行case,直接获得数据
                dependent_util = DependentData(response_data)
                # 获得相应数据
                value = dependent_util.get_need_value(dependent_data, response_type)
                # 写入对应json中
                self.json.set_data(request_data, target_data, value)
            else:
                pass

        data = self.data.get_data_from_json(row, json_file_name=self.json_file_name)
        if is_cookie == 'write':
            res = self.run_method.run_main(method, url, data, header)
            self.cookie = getCookies(method, url, data, header)
            result['cookie'] = self.cookie
        elif is_cookie == 'yes':
            res = self.run_method.run_main(method, url, data, header, self.cookie)
        else:
            res = self.run_method.run_main(method, url, data, header)

        response_type = self.data.get_response_type(row)

        # 根据类型写入数据到返回结果中
        if response_type == "HTML":
            op_html = OperationHtml(case_id+".html", res.text, is_write=True)
            self.result_data.write_result(row, op_html.get_root_path())
            result['result'] = op_html.get_root_path()
        else:
            self.result_data.write_result(row, res.text)
            result['result'] = res.text

        if self.com_util.is_contain(expect, res.text):
            self.result_data.write_isPass(row, "pass")
            self.pass_count.append(row)
            result['is_pass'] = 'pass'
        else:
            self.result_data.write_isPass(row, "fail")
            self.fail_count.append(row)
            result['is_pass'] = 'fail'

        return result

    # 程序执行的主入口
    def go_on_run(self, data_file_name, json_file_name):

        self.data_file_name = data_file_name
        self.json_file_name = json_file_name
        rows_count = self.data.get_case_lines()
        print(rows_count)
        res = None

        print("-------start-------")
        for i in range(2, rows_count+1):
            # case是否要运行
            is_run = self.data.get_is_run(i)
            if is_run:
                print("----------" + str(i-1) + "start-----------")
                self.run_it_by_row_num(i)
                print("----------" + str(i-1) + "end-----------")

        # self.send_mail.send_main(pass_count, fail_count)
        return res


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
