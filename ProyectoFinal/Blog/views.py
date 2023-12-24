from audioop import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Comentario 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from .forms import ComentarioForm
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator


def Blogs(request):
    return render (request, 'Blog/blog.html')

##MODELO BLOG##
    
class BlogCreate(LoginRequiredMixin,CreateView):

    model= Blog
    template_name='Blog/blog_crear.html'
    fields= ["titulo", "descripcion", "autor", "categoria", "imagen", "Fecha"]
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
    fields=["titulo", "descripcion", "autor", "categoria", "imagen", "Fecha"]

    def get_object(self,queryset=None):
        user_id= self.request.user.pk
        return get_object_or_404(Blog, pk=self.kwargs['pk'], usuario_id=user_id)
    
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
@method_decorator(login_required, name='dispatch')  
class ComentarioCreate(LoginRequiredMixin, CreateView):
    template_name = 'Comentarios/comentario_create.html'

    def get(self, request, blog_pk):
        blog = get_object_or_404(Blog, pk=blog_pk)
        form = ComentarioForm()
        return render(request, self.template_name, {'blog': blog, 'form': form})

    def post(self, request, blog_pk):
        blog = get_object_or_404(Blog, pk=blog_pk)
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.blog = blog
            comentario.save()
            return redirect(f"blog_list")
        return render(request, self.template_name, {'blog': blog, 'form': form})
   
    



