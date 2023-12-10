
from django.urls import path
from hr import views

urlpatterns = [

    path("signin",views.SigninView.as_view(),name="signin"),
    path("index",views.DashBoardView.as_view(),name="index"),
    path("signout",views.SignOutView.as_view(),name="signout"),
    path("category",views.CategoryListCreateView.as_view(),name="category"),
    path("category/<int:pk>/remove",views.CategoryDeleteView.as_view(),name="category-delete"),
    path("jobs/add",views.JobCreateView.as_view(),name="job-add"),
    path("jobs/all",views.JobListView.as_view(),name="job-list"),
    path("jobs/<int:pk>/remove",views.JobDeleteView.as_view(),name="job-delete"),
    path("jobs/<int:pk>/change",views.JobUpdateView.as_view(),name="job-edit"),

   
]