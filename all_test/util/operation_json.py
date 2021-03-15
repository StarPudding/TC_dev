# coding: utf-8
import json
from all_test.util.CommonUtil import CommonUtil

class OperationJson:
    def __init__(self, file_name=None):
        if file_name is None:
            self.file_name = '../dataConfig/login.json'
            self.data = self.read_data()
        else:
            self.file_name = file_name
            self.data = self.read_data()
        self.data_split = ';\n'

    def read_data(self):
        with open(self.file_name, 'rb') as fp:
            data = json.load(fp)
            return data

    def get_data(self, id):
        return self.data[id]

    def set_data(self, main_id, id_input, values):
        ids = id_input.split(self.data_split)
        print(ids)
        common_util = CommonUtil()
        count = 0
        for id in ids:
            # 假如id是数组类型 如test[].xx
            if common_util.is_contain("[]", id):
                # 暂时只支持数组里面只有一位
                temp = id.split('[')
                id = temp[0]+"["+str(0)+temp[1]
            else:
                id = id
            print(id)
            print(values)
            if values is None:
                self.data[main_id][id] = ""
            else:
                self.data[main_id][id] = values[count]
            count = count + 1
            with open(self.file_name, 'w', encoding='utf-8') as fp:
                fp.write(json.dumps(self.data, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    op = OperationJson()
    op.set_data('forecast_update', 'id', '310')


