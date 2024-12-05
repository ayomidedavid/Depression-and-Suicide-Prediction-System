from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('depression_result/', views.depression, name='depression'),
    path('suicide', views.home2, name='home2'),
    path('suicide_result/', views.suicide, name='suicide'),
]
