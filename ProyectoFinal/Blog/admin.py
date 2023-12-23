from django.contrib import admin
from . import models

admin.site.register(models.Blog)
admin.site.register(models.Comentario)
admin.site.register(models.Perfil)
