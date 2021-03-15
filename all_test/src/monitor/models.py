from django.utils.http import urlquote
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref

# 以下是sqlalchemy
Base = declarative_base()
# 此处定义要使用的数据库
str = "mysql+mysqldb://tester:%s@192.168.220.140:3306/testcenter?charset=utf8" % urlquote('test@123')
engine = create_engine(str, echo=True, max_overflow=5)


# 定义表结构
class warehouse_monitor(Base):
    __tablename__ = 'warehouse_monitor'

    warehouse_name = Column(String, primary_key=True)
    max_online = Column(Integer, nullable=False)
    last_online = Column(Integer, nullable=False)
    last_offline = Column(Integer, nullable=False)
    last_offline_list = Column(String(255), nullable=True)
    is_check = Column(Integer, nullable=True)
    last_check_time = Column(Integer, nullable=True)