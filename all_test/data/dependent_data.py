#coding:utf-8


from all_test.util.operation_html import OperationHtml


class DependentData:
    def __init__(self, response_data):
        self.data = response_data
        self.data_split = ';\n'
        self.key_value_split = ":"

    def get_need_value(self, data_position=None, response_type=None):
        if response_type == 'HTML':
            # 从文件服务器或者项目目录里取到html文件
            return self.get_value_from_HTML(data_position)

    # data_num代表要从HTML里面取多少数据
    def get_value_from_HTML(self, data_position=None, data_num=None):
        html = OperationHtml(self.data)
        # 多条数据
        datas = str(data_position).split(self.data_split)
        out = []
        for data in datas:
            # 单条数据
            strs = str(data).split(self.key_value_split)
            type = strs[0]
            value = strs[1]
            result = html.GetValue(type, value)
            if len(result) is not 0:
                out.append(result[0])
            else:
                out.append("")
        # print(out)
        return out





