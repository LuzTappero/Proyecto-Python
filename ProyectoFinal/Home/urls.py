
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about_me/', views.About, name='about_me'),
    path('registro/', views.registro_view, name='registro'), 
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='Home/logout.html'), name='logout'),
    path ('profile/<id>', views.profile_view, name='profile'), 
    path('profile_create/',views.profile_create, name='profile_create'),
    path('profile_update/', views.profile_update, name= 'profile_update'), # type: ignore
    path('crear_avatar/', views.crear_avatar, name= 'crear_avatar'), # type: ignore
    path('update_avatar/', views.update_avatar, name='update_avatar')
   
    ]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)