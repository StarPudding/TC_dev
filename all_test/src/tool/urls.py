from django.urls import path
from all_test.src.tool import views

urlpatterns = [
    path(r'CombineSQLAndParameter/', views.CombineSQLAndParameter),
]
