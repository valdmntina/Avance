from django import forms
from .models import Formulario, Serpientes

class Form(forms.ModelForm):
    class Meta: #subclase 
        model = Formulario
        fields = ['nombre', 'apellido', 'telefono', 'correo']


