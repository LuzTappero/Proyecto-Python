from django.db import models
from django.contrib.auth.models import User
from Home.models import Avatar
from datetime import date

class Perfil (models.Model):
    usuario= models.ForeignKey(User, on_delete= models.CASCADE)
    about_me= models.CharField(max_length=2200)


    def __str__(self):
        return f"{self.usuario}"

class Blog(models.Model):
    titulo= models.CharField(max_length=255)
    descripcion= models.CharField(max_length=5000)
    imagen= models.FileField(upload_to= 'media/blogs', null=True, blank=True)
    Fecha= models.DateField(default=date.today)
    autor=models.CharField(max_length=255)
    categoria= models.CharField(max_length=255)
    usuario= models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    texto= models.CharField(max_length=2500) 
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"@{self.usuario}: '{self.blog}'"
    


