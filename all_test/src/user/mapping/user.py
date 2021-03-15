from django.db import connection


def isUserExists(username, password):
    cursor = connection.cursor()
    sql = "select * from test_user where username='" + username + "' and password='" + password + "';"
    print(sql)
    n = cursor.execute(sql)
    # 返回的结果
    if n != 0:
        return True
    else:
        return False
