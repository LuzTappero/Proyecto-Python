from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import UserCreationFormulario, UserEditionFormulario, UserAvatarFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from .models import Avatar
from Blog.models import User, Blog #Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from datetime import datetime
from django.urls import reverse_lazy
from Blog.models import Perfil
from django.views.generic.detail import DetailView



def Home(request):
    if request.user.is_authenticated:
        usuario= request.user
        avatar = Avatar.objects.filter(user=usuario).first()
        avatar_url= avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url=""
    return render (request, 'Home/index.html', context= {'avatar_url':avatar_url})

def About(request):
    return render (request, 'Home/aboutme.html')

def registro_view(request):

    if request.method == "GET":
        return render (request,
                    'Home/registro.html',
                     {"form": UserCreationFormulario()})
    else:
        formulario= UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario= informacion ["username"]
            formulario.save()

            return render (request, 'Home/inicio.html', {"mensaje": f"Usuario creado: {usuario}"})
        else:
            return render (request, 'Home/registro.html', {"form":formulario})

def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            'Home/inicio.html',
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            'Home/login.html',
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(request,
                'Home/inicio.html', 
                {"mensaje": f"Bienvenido {usuario}"}) 
        else:
            return render(
                request,
                'Home/login.html',
                {"form": formulario}
            )

def logout_view(request):
    pass

def profile_view(request, id=None):
    if id:
        user= User.objects.get(id=id)
        profile= Perfil.objects.filter(usuario=user).first()
        avatar= Avatar.objects.filter(user=user).first()
        avatar_url= avatar.imagen.url if avatar is not None else ""
        context= {'profile': profile, 'avatar_url': avatar_url}

        return render (request, 'Home/profile.html', context)
    else:
        return HttpResponse("Id no proporcionado en la URL.")

@login_required
def profile_update(request):

    usuario= request.user
    perfil= Perfil.objects.filter(usuario=usuario).last()
    # avatar = Avatar.objects.filter(user=usuario).last()
    # avatar_url= avatar.imagen.url if avatar is not None else ""

    if request.method == "GET":

        valores_iniciales = {
            "email": usuario.email,
            "about_me": perfil.about_me if perfil else ""
        }

        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            'Home/profile_update.html',
            context={"form": formulario, "usuario": usuario, "profile":perfil}
            )
    elif request.method == "POST":
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.set_password(informacion["password1"])
            if perfil:
                perfil.about_me = informacion["about_me"]
                perfil.save()

            usuario.save()
            return redirect('profile', id=usuario.id)
    else:
        return HttpResponseBadRequest('Bad Request')
    
@login_required # type: ignore
def crear_avatar(request):
    usuario = request.user

    if request.method == "GET":
        formulario = UserAvatarFormulario()
        return render(
            request,
            'Home/crear_avatar.html',
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = UserAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Avatar(user=usuario, imagen=informacion["imagen"])
            modelo.save()
            return redirect('Home: index')
        
