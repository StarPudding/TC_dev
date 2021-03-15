from django.urls import path
from all_test.src.testCase.interface import TestCase

urlpatterns = [
    path(r'TestCase/UploadFile/', TestCase.UploadFile),
    path(r'TestCase/TestOne/', TestCase.TestOne),
]

