"""all_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from all_test import views
from all_test.src.monitor.interface import wms_app_monitor
from all_test.src.testCase.interface import TestCase
from all_test.src.user.interface import user
from django.views.generic import TemplateView


urlpatterns = [
    path(r'^admin/', admin.site.urls),

    # 监控
    path(r'monitor/', include('all_test.src.monitor.urls')),

    # 测试
    path(r'TestCase/', include('all_test.src.testCase.urls')),

    # 版本发布
    path(r'VersionControl/', include('all_test.src.versionControl.urls')),

    # 系统设置
    path(r'system/', include('all_test.src.system.urls')),

    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^hello', views.hello),


    url(r'user/login/', user.login),

    url(r'Tool/', include('all_test.src.tool.urls'))
]
