from django.urls import path, include

from . import views

urlpatterns = [
  path('user/register', views.registerUser, name='register'),
  path('user/login', views.login, name='login')
]
