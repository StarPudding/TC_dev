from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
# from all_test.src.system.models import sys_project, sys_environment, sys_project_environment
from all_test.src.system.acl_models import engine
from all_test.src.monitor.models import warehouse_monitor

Session = sessionmaker(bind=engine)
session = Session()


def initStatus():
    outs = session.query(warehouse_monitor).all()
    for out in outs:
        out.is_check = 0
    session.commit()


def addMessage(warehouse_name, online, offline, offline_list=None, is_check=1, check_time=None):
    # ret = session.query(exists().where(warehouse_monitor.warehouse_name == warehouse_name)).scalar()
    rets = session.query(warehouse_monitor).filter_by(warehouse_name=warehouse_name)
    count = rets.count()
    if count != 0:
        ret = session.query(warehouse_monitor).get(warehouse_name)
        if online > ret.max_online:
            ret.max_online = online
        ret.last_online = online
        ret.last_offline = offline
        ret.last_offline_list = offline_list
        ret.is_check = is_check
        ret.last_check_time = check_time
        session.commit()
    else:
        w = warehouse_monitor(warehouse_name=warehouse_name,
                              max_online=online,
                              last_online=online,
                              last_offline=offline,
                              last_offline_list=offline_list,
                              is_check=is_check,
                              last_check_time=check_time)
        session.add(w)
        session.commit()


def getMessage(status=None, warehouse_name=None):
    condition = []
    out = ''
    if warehouse_name is not None and warehouse_name is not '':
        condition.append(warehouse_monitor.warehouse_name == warehouse_name)
    if status == 0:
        out = session.query(warehouse_monitor.warehouse_name.label('warehouse_name'),
                            warehouse_monitor.max_online.label('max_online'),
                            warehouse_monitor.last_online.label('last_online'),
                            warehouse_monitor.is_check.label('is_check'),
                            warehouse_monitor.last_check_time.label('last_check_time')).filter(*condition)
    elif status == 1:
        # 正常
        condition.append(warehouse_monitor.max_online == warehouse_monitor.last_online)
        condition.append(warehouse_monitor.last_check_time != None)
        out = session.query(warehouse_monitor.warehouse_name.label('warehouse_name'),
                            warehouse_monitor.max_online.label('max_online'),
                            warehouse_monitor.last_online.label('last_online'),
                            warehouse_monitor.is_check.label('is_check'),
                            warehouse_monitor.last_check_time.label('last_check_time')).filter(*condition)
    elif status == 2:
        # 异常
        condition.append(warehouse_monitor.max_online != warehouse_monitor.last_online)
        condition.append(warehouse_monitor.last_check_time != None)
        out = session.query(warehouse_monitor.warehouse_name.label('warehouse_name'),
                            warehouse_monitor.max_online.label('max_online'),
                            warehouse_monitor.last_online.label('last_online'),
                            warehouse_monitor.is_check.label('is_check'),
                            warehouse_monitor.last_check_time.label('last_check_time')).filter(*condition)
    elif status == 3:
        # 未被检查
        condition.append(warehouse_monitor.last_check_time == None)
        out = session.query(warehouse_monitor.warehouse_name.label('warehouse_name'),
                            warehouse_monitor.max_online.label('max_online'),
                            warehouse_monitor.last_online.label('last_online'),
                            warehouse_monitor.is_check.label('is_check'),
                            warehouse_monitor.last_check_time.label('last_check_time')).filter(*condition)
    else:
        out = session.query(warehouse_monitor.warehouse_name.label('warehouse_name'),
                            warehouse_monitor.max_online.label('max_online'),
                            warehouse_monitor.last_online.label('last_online'),
                            warehouse_monitor.is_check.label('is_check'),
                            warehouse_monitor.last_check_time.label('last_check_time')).filter(*condition)[0]
    return out


def getNotCheckWarehouseName():
    items = session.query(warehouse_monitor).filter(warehouse_monitor.is_check == 0).all()
    out = []
    for item in items:
        out.append(item.warehouse_name)
    return out


def getAllWarehouseName():
    out = session.query(warehouse_monitor.warehouse_name.label('warehouse_name')).all()
    return out


def updateCheckTime(warehouse_name):
    rets = session.query(warehouse_monitor).filter_by(warehouse_name=warehouse_name)
    count = rets.count()
    if count != 0:
        ret = session.query(warehouse_monitor).get(warehouse_name)
        ret.last_check_time = None
        session.commit()


if __name__ == '__main__':
    out1 = getAllWarehouseName()
    for out11 in out1:
        print(out11)
