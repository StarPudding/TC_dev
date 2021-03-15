from all_test.src.system.models import sys_environment


def getAllEnvironmentOfProject(project_id):
    out = sys_environment.objects.raw('SELECT b.environment_id, b.environment_name '
                                      'FROM sys_environment b WHERE '
                                      'b.environment_id IN ( '
                                      'SELECT environment_id FROM sys_project_environment '
                                      'WHERE project_id=%s )', params=[project_id,])
    return out
