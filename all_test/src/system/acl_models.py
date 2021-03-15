from django.utils.http import urlquote
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from all_test.setting.base import DATABASES
# 以下是sqlalchemy
Base = declarative_base()
# 此处定义要使用的数据库
# str = "mysql+mysqldb://tester:%s@" % urlquote('test@123') + DATABASES.get('default').get('HOST') + \
#       ":3306/testcenter?charset=utf8"
str = "mysql+mysqldb://root:%s@" % urlquote('root') + DATABASES.get('default').get('HOST') + \
      ":3306/testcenter?charset=utf8"
engine = create_engine(str, echo=True, max_overflow=5)


# 定义表结构
class sys_project(Base):
    __tablename__ = 'sys_project'

    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(50), nullable=True)


class sys_environment(Base):
    __tablename__ = 'sys_environment'
    environment_id = Column(Integer, primary_key=True)
    environment_name = Column(String(50), nullable=True)


class sys_project_environment(Base):
    __tablename__ = 'sys_project_environment'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer)
    environment_id = Column(Integer)
    svn_position = Column(String(255), nullable=True)
    project_position = Column(String(255), nullable=True)
    svn_username = Column(String(255), nullable=True)
    svn_password = Column(String(255), nullable=True)
    jenkins_url = Column(String(255), nullable=True)
    jenkins_job = Column(String(255), nullable=True)
    jenkins_username = Column(String(255), nullable=True)
    jenkins_password = Column(String(255), nullable=True)



