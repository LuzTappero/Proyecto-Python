from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('Blogs/', views.Blogs, name='Blogs'),
    path ('blog_create/', views.BlogCreate.as_view(), name='blog_create'),
    path ('blog_list/', views.BlogList.as_view(), name='blog_list'),
    path ('blog_update/<pk>', views.BlogUpdate.as_view(), name='blog_update'),
    path ('blog_delete/<pk>', views.BlogDelete.as_view(), name='blog_delete'),
    path('mis_blog_list/<id>/', views.MisBlogList, name= 'mis_blog_list'),
    
    path ('comentario_create/<int:blog_pk>', views.ComentarioCreate.as_view(), name='comentario_create')
    ]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)