
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path ('Blogs/', views.Blogs, name='Blogs'),
    
    #URLs para interacción con base de datos
    #modeloComentario

    path ('blog_create/', views.BlogCreate.as_view(), name='blog_create'),
    path ('blog_list/', views.BlogList.as_view(), name='blog_list'),
    path ('blog_update/<pk>', views.BlogUpdate.as_view(), name='blog_update'),
    path ('blog_delete/<pk>', views.BlogDelete.as_view(), name='blog_delete'),
    
    
    #URLs para interacción con base de datos
    #modelComentario
    # path ('comentario_create/<int:pk>', views.ComentarioCreate.as_view(), name='comentario_create'),
    # path ('comentario_list/', views.ComentarioList.as_view(), name='comentario_list'),
    # path ('comentario_update/<pk>', views.ComentarioUpdate.as_view(), name='comentario_update'),
    # path ('comentario_delete/<pk>', views.ComentarioDelete.as_view(), name= 'comentario_delete')
    ]

    