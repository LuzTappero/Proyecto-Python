
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about_me/', views.About, name='about_me'),
    path('registro/', views.registro_view, name='registro'), #type:ignore
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='Home/logout.html'), name='logout'),
    path('profile_update/', views.profile_update, name= 'profile_update'), # type: ignore
    path('crear_avatar/', views.crear_avatar, name= 'crear_avatar'), # type: ignore
    path ('profile/<id>', views.profile_view, name='profile') # type: ignore
    ]