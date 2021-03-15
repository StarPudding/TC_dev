# coding:utf-8


class global_var:
    # case id
    Id = 1
    request_name = 2
    url = 3
    run = 4
    request_way = 5
    header = 6
    cookie = 7
    case_depend = 8
    data_depend = 9
    field_depend = 10
    data = 11
    expect = 12
    result = 13
    isPass = 14
    response_type = 15  # 返回数据的类型(决定用哪种方法来找)

    header_value = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }

    cookie_value = None


# 获取caseid
def get_id():
    return global_var.Id


# 获取name
def get_name():
    return global_var.request_name


# 获取url
def get_url():
    return global_var.url


def get_run():
    return global_var.run


def get_run_way():
    return global_var.request_way


def get_header():
    return global_var.header


def get_case_depend():
    return global_var.case_depend


def get_data_depend():
    return global_var.data_depend


def get_field_depend():
    return global_var.field_depend


def get_data():
    return global_var.data


def get_expect():
    return global_var.expect


def get_result():
    return global_var.result


def get_isPass():
    return global_var.isPass


def get_response_type():
    return global_var.response_type


def get_header_value():
    return global_var.header_value


def set_header_value(key, value):
    global_var.header_value[key] = value


def get_cookie():
    return global_var.cookie


def set_cookie(cookie_value):
    global_var.cookie_value = cookie_value
