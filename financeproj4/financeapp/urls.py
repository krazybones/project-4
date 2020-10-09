from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register')
]
