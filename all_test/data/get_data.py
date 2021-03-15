# coding:utf-8

from all_test.util.operation_excel_plus import OperationExcel
import all_test.data.data_config as data_config
from all_test.util.operation_json import OperationJson


class GetData:
    def __init__(self, file_name=None, sheet_id=None, copy_file_name=None):
        self.opera_excel = OperationExcel(file_name=file_name, sheet_id=sheet_id, copy_file_name=copy_file_name)

    # 获取excel行数，也就是case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取id
    def get_case_id(self, row):
        col = data_config.get_id()
        case_id = self.opera_excel.get_cell_value(row, col)
        return case_id

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = data_config.get_run()
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = data_config.get_header()
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    # 是否需要cookie
    def is_cookie(self, row):
        col = data_config.get_cookie()
        cookie = self.opera_excel.get_cell_value(row, col)
        return cookie

    # 获取请求方式
    def get_request_method(self, row):
        col = data_config.get_run_way()
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = data_config.get_url()
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = data_config.get_data()

        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 通过获取关键字拿到data数据
    def get_data_from_json(self, row, json_file_name):
        opera_json = OperationJson(json_file_name)

        request_data = opera_json.get_data(self.get_request_data(row))

        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = data_config.get_expect()
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    # 写入实际结果
    def write_result(self, row, value):
        col = data_config.get_result()
        self.opera_excel.write_value(row, col, value)
        return True

    # 获得实际结果
    def get_result(self, row):
        col = data_config.get_result()
        result = self.opera_excel.get_cell_value(row, col)
        if result == '':
            return None
        return result

    # 获得是否通过
    def get_isPass(self, row):
        col = data_config.get_isPass()
        is_pass = self.opera_excel.get_cell_value(row, col)
        if is_pass == '':
            return None
        return is_pass

    # 写入是否通过
    def write_isPass(self, row, value):
        col = data_config.get_isPass()
        self.opera_excel.write_value(row, col, value)
        return True

    # 获取依赖case
    def get_depend_case(self, row):
        col = int(data_config.get_case_depend())
        dependent_case = self.opera_excel.get_cell_value(row, col)
        if dependent_case == '':
            return None
        else:
            return dependent_case

    # 获取依赖数据
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend())
        dependent_key = self.opera_excel.get_cell_value(row, col)
        if dependent_key == '':
            return None
        else:
            return dependent_key

    # 获取目标数据
    def get_depend_field(self, row):
        col = int(data_config.get_field_depend())
        dependent_field = self.opera_excel.get_cell_value(row, col)
        if dependent_field == '':
            return None
        else:
            return dependent_field

    # 获取返回数据类型
    def get_response_type(self, row):
        col = int(data_config.get_response_type())
        result = self.opera_excel.get_cell_value(row, col)
        if result == '':
            return None
        else:
            return result

    # # 写入依赖数据
    # def write_dependent_data(self, ):