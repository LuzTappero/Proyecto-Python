##Registro de usuarios

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from django import forms
from .models import Avatar


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label= "Contraseña", widget= forms.PasswordInput )
    password2= forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:
        model=UserModel
        fields= ["password1", "password2", "username", "email"]
        help_text= {k: "" for k in fields}

class UserEditionFormulario(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir Contraseña", widget=forms.PasswordInput)


    class Meta:
        model = UserModel
        fields = ["email", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}

class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model= Avatar
        fields= ["imagen"]