from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


# user表
class TestUser(Base):
    __tablename__ = 'test_user'

    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(20))
