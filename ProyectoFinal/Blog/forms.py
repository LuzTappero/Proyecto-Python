from .models import Comentario
from django import forms

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {'texto': forms.Textarea(attrs={'rows': 3}),}