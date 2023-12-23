from django.shortcuts import render, redirect
from .models import Blog #Comentario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def Blogs(request):
    return render (request, 'Blog/blog.html')

####VISTAS BASADAS EN CLASES####

##MODELO BLOG##
    
class BlogCreate(LoginRequiredMixin,CreateView):

    model= Blog
    template_name='Blog/blog_crear.html'
    fields= ["titulo", "descripcion", "autor", "categoria"]
    success_url= '/blog_list/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class BlogList(ListView):
    
    model= Blog
    template_name= 'Blog/blog_list.html'
    context_object_name='blogs'

class BlogUpdate(UpdateView):
    
    model= Blog
    template_name = 'Blog/blog_update.html'
    fields=["titulo", "descripcion", "autor", "categoria"]
    success_url= '/blog_list/'

class BlogDelete(DeleteView):
    
    model= Blog
    template_name = 'Blog/blog_delete.html'
    success_url= '/blog_list/'

##MODELO COMENTARIO##
    
# class ComentarioCreate(CreateView):
#     pass
#     model= Comentario
#     template_name= 'Comentarios/comentario_create.html'
#     fields= ["nombre", "edad", "comentario"]
#     success_url= '/comentario_list/'

# class ComentarioList(ListView):
    
#     model= Comentario
#     template_name= 'Comentarios/comentario_list.html'
#     context_object_name='comentarios'

# class ComentarioUpdate(UpdateView):
    
#     model= Comentario
#     template_name = 'Comentarios/comentario_update.html'
#     fields=["nombre", "edad", "comentario"]
#     success_url= '/comentario_list/'

# class ComentarioDelete(DeleteView):
    
#     model= Comentario
#     template_name = 'Comentarios/comentario_delete.html'
#     success_url= '/comentario_list/'


