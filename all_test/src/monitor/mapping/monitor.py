from django.db import connection
from all_test.base.run_method import RunMethod


def getAllMonitor(warehouse_name):
    cursor = connection.cursor()
    if warehouse_name is not '':
        sql = "select monitor_id, monitor_name,last_offline_date from monitor_list where monitor_belong = '" + warehouse_name + "'"
    else:
        sql = "select monitor_id, monitor_name,last_offline_date from monitor_list"
    n = cursor.execute(sql)
    # 返回的结果
    results = []

    for i in range(0, n):
        data = cursor.fetchone()
        result = {'monitor_id': data[0], 'monitor_name': data[1], 'last_offline_date': data[2]}
        results.append(result)
    return results


def getMonitorById(monitor_id):
    cursor = connection.cursor()
    sql = "select monitor_url, sysCode from monitor_list where monitor_id = '" + monitor_id + "'"
    cursor.execute(sql)
    data = cursor.fetchone()
    result = {'monitor_url': data[0], 'sysCode': data[1]}
    return result

