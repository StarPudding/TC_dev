from django.db import connection
from all_test.src.system.models import menu


def getAllRootMenu():
    out = menu.objects.filter(parent_id=0).order_by('sort_id')
    return out


def getMenuById(menu_id):
    out = menu.objects.filter(menu_id=menu_id)
    return out


def getChild(parent_id):
    out = menu.objects.filter(parent_id=parent_id).order_by('sort_id')
    return out


def addMenu(menu_info):
    print(menu_info)
    out = menu.objects.create(**menu_info)
    print(out.menu_id)
    return out


def addChild(parent_id, child_id):
    parent = menu.objects.get(menu_id=parent_id)
    if parent.child is None or parent.child == '':
        parent.child = str(child_id)
    else:
        parent.child = str(parent.child) + ',' + str(child_id)
    parent.save()
    return


def updateMenu(menu_info):
    id = menu_info['menu_id']
    out = menu.objects.filter(menu_id=id).update(**menu_info)
    return out


def deleteMenu(menu_id):
    out = menu.objects.filter(menu_id=menu_id).delete()
    return out

