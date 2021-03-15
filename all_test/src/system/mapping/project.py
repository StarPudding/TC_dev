from all_test.src.system.models import sys_project


def getAllProject():
    out = sys_project.objects.all()

    return out
