# coding:utf-8

class CommonUtil:
    def is_contain(self, str_one, str_two):
        # 判断一个字符串是否在另一个字符串中
        flag = None
        if type(str_one) is float:
            str_one = int(str_one)
        str_one = str(str_one)
        str_two = str(str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
