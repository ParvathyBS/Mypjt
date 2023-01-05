from . import views
from django.urls import path

app_name = 'mypjtapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_person/', views.person, name="person"),
    path('branches/', views.branches, name="branches"),
    path('details/', views.details, name="details"),
]
