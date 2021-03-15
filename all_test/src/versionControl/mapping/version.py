from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
# from all_test.src.system.models import sys_project, sys_environment, sys_project_environment
from all_test.src.versionControl.models import engine, s_commondata


Session = sessionmaker(bind=engine)
session = Session()


def getAllProjects():
    out = session.query(s_commondata.CodeValue.label('CodeValue')).filter(s_commondata.CodeKey=='platform')

    return out


if __name__ == '__main__':
    getAllProjects()
