from sqlalchemy.orm import sessionmaker

# from all_test.src.system.models import sys_project, sys_environment, sys_project_environment
from all_test.src.system.acl_models import engine, sys_project_environment, sys_project, sys_environment

Session = sessionmaker(bind=engine)
session = Session()


def getSVNInfo(project_id, environment_id):
    out = session.query(sys_project_environment).filter_by(project_id=project_id, environment_id=environment_id)
    return out


def getAllMainInfo(project_id, environment_id):
    condition = []
    if project_id is not None and project_id is not '':
        condition.append(sys_project_environment.project_id == project_id)
    if environment_id is not None and environment_id is not '':
        condition.append(sys_project_environment.environment_id == environment_id)
    out = session.query(sys_project_environment.id.label('id'),
                        sys_project.project_id.label('project_id'),
                        sys_project.project_name.label('project_name'),
                        sys_environment.environment_id.label('environment_id'),
                        sys_environment.environment_name.label('environment_name')) \
        .join(sys_project, sys_project.project_id == sys_project_environment.project_id) \
        .join(sys_environment, sys_environment.environment_id == sys_project_environment.environment_id)\
        .filter(*condition)
    return out


def getMainInfo(id):
    out = session.query(sys_project_environment.project_position.label('project_position'),
                        sys_project_environment.svn_position.label('svn_position'),
                        sys_project_environment.jenkins_job.label('jenkins_job'),
                        sys_project_environment.jenkins_url.label('jenkins_url')) \
        .filter(sys_project_environment.id == id)
    return out
# def getSVNInfo(project_id, environment_id):
#     out = sys_project_environment.objects.filter(project_id=project_id, environment_id=environment_id)
#     return out
#
#
# def getAllMainInfo(project_id, environment_id):
#     kwargs = {}
#     if project_id is not None and project_id is not '':
#         kwargs['name__startWith'] = project_id
#     if environment_id is not None and environment_id is not '':
#         kwargs['address__contains'] = environment_id
#     out = sys_project_environment.objects.raw('''SELECT
#                                                     n.id,
#                                                     n.project_id,
#                                                     n.project_name,
#                                                     e.environment_id,
#                                                     e.environment_name
#                                                 FROM
#                                                     sys_environment e
#                                                     INNER JOIN (
#                                                     SELECT
#                                                         t.id,
#                                                         p.project_id AS project_id,
#                                                         p.project_name AS project_name,
#                                                         t.environment_id AS environment_id
#                                                     FROM
#                                                         sys_project_environment t
#                                                     INNER JOIN sys_project p ON p.project_id = t.project_id
#                                                     ) AS n ON e.environment_id = n.environment_id''').filter(**kwargs)
#
#     return out
