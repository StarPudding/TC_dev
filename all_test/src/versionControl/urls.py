from django.urls import path
from all_test.src.versionControl import views

urlpatterns = [
    path(r'Update/', views.UpdateVersion),
    path(r'Combine/', views.CombineVersion),
    path(r'Commit/', views.CommitVersion),
    path(r'Revert/', views.RevertVersion),
    path(r'Cleanup/', views.CleanupVersion),
    path(r'Log/', views.ListLog),
    path(r'Jenkins_build/', views.JenkinsBuild),
    path(r'getAllProjects/', views.getAllProjects),
    path(r'getSVNVersionList/', views.getSVNVersionList)
]
