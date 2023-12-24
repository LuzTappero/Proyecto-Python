##Registro de usuarios

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from django import forms
from .models import Avatar
from Blog.models import Perfil


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label= "Contraseña", widget= forms.PasswordInput )
    password2= forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:
        model=UserModel
        fields= ["password1", "password2", "username", "email"]
        help_text= {k: "" for k in fields}

class UserEditionFormulario(UserChangeForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email"]
        help_texts = {k: "" for k in fields}

    about_me= forms.CharField()


class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model= Avatar
        fields= ["imagen"]
        
class PerfilFormulario(forms.ModelForm):

    class Meta:
        model= Perfil
        fields= ["usuario", "about_me"]
