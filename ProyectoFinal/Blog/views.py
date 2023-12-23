from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog #Comentario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User



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

class BlogUpdate(LoginRequiredMixin,UpdateView):
    
    model= Blog
    template_name = 'Blog/blog_update.html'
    fields=["titulo", "descripcion", "autor", "categoria"]

    def get_success_url(self):
        user_id= self.request.user.pk
        return f'/mis_blog_list/{user_id}'

class BlogDelete(LoginRequiredMixin, DeleteView):
    
    model= Blog
    template_name = 'Blog/blog_delete.html'
    def get_success_url(self):
        user_id= self.request.user.pk
        return f'/mis_blog_list/{user_id}'

@login_required
def MisBlogList(request, id=None):
    if id:
        user = User.objects.get(id=id)
        mis_blogs = Blog.objects.filter(usuario= user).all()
        context= {'blogs': mis_blogs}
        return render (request, 'Blog/mis_blog_list.html', context)
    else:
         # Lógica si id no está presente
        return HttpResponse("ID no proporcionado en la URL.")


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


