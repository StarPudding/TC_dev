from django.utils.http import urlquote
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref

# 以下是sqlalchemy
Base = declarative_base()
# 此处定义要使用的数据库
str = "mysql+mysqldb://root:%s@localhost:3306/version_test?charset=utf8" % urlquote('root')
engine = create_engine(str, echo=True, max_overflow=5)


# 定义表结构
class s_commondata(Base):
    __tablename__ = 's_commondata'

    id = Column(Integer, primary_key=True)
    CodeName = Column(String, nullable=False)
    CodeKey = Column(String, nullable=False)
    CodeCode = Column(String, nullable=False)
    CodeSort = Column(String, nullable=True)
    CodeValue = Column(String, nullable=True)
    Remark = Column(String, nullable=False)
