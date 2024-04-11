from django import forms
from .models import Formulario

class Form(forms.ModelForm):
    class Meta: #subclase 
        model = Formulario
        fields = ['nombre', 'apellido', 'telefono', 'correo']
