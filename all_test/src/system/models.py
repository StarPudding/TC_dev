from django.db import models


# 用户表
class user(models.Model):
    id = models.AutoField(max_length=11, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    count = models.IntegerField(max_length=255)

    class Meta:
        db_table = 'menu'


# 菜单表
class menu(models.Model):
    menu_id = models.AutoField(max_length=5, primary_key=True)
    menu_name = models.CharField(max_length=50)
    menu_url = models.CharField(max_length=50)
    parent_id = models.IntegerField(max_length=5)
    sort_id = models.IntegerField(max_length=5)
    is_show = models.IntegerField(max_length=1)
    authority = models.CharField(max_length=50)
    menu_icon = models.CharField(max_length=50)

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'menu'


class sys_project(models.Model):
    project_id = models.AutoField(max_length=5, primary_key=True)
    project_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sys_project'


class sys_environment(models.Model):
    environment_id = models.AutoField(max_length=5, primary_key=True)
    environment_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sys_environment'


class sys_project_environment(models.Model):
    id = models.AutoField(max_length=5, primary_key=True)
    project_id = models.IntegerField(max_length=5)
    environment_id = models.IntegerField(max_length=5)
    svn_position = models.CharField(max_length=255)
    project_position = models.CharField(max_length=255)
    svn_username = models.CharField(max_length=255)
    svn_password = models.CharField(max_length=255)
    jenkins_url = models.CharField(max_length=255)
    jenkins_job = models.CharField(max_length=50)
    jenkins_username = models.CharField(max_length=50)
    jenkins_password = models.CharField(max_length=50)

    class Meta:
        db_table = 'sys_project_environment'


