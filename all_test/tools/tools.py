
def CombineSQLAndParameter(sql, parameter):
    result = ''
    parameters = parameter.split(',')
    parm_result = []
    for item in parameters:
        parm_result.append(item.split('(')[0])
    count = 0
    for i in sql:
        if i == '?' or i == '？':
            result = result + parm_result[count]
            count = count + 1
        else:
            result = result + i
    return result
