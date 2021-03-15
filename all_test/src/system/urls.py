from django.urls import path
from all_test.src.system import views

urlpatterns = [
    path(r'menu/', views.getMenu),
    path(r'get_child_menu/', views.getChildMenu),
    path(r'add_child_menu/', views.addChildMenu),
    path(r'update_menu/', views.updateMenu),
    path(r'delete_menu/', views.deleteMenu),
    path(r'get_all_menu/', views.getAllMenu),

    path(r'get_all_project/', views.getAllProject),
    path(r'get_environment_by_project/', views.getEnvironmentOfProject),
    path(r'getAllProjectAndEnvironment/', views.getAllProjectAndEnvironment),
    path(r'getMainInfo/', views.getMainInfo),

    path(r'get_user/', views.getUser)

]
