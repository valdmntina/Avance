from django import forms
from .models import Formulario

#define la clase del formulario que hereda de modelform
class Form(forms.ModelForm):
    #subclase meta que proporciona metadatos para el formulario
    class Meta: #subclase 
        #aqui especifica el modelo al que esta asociado
        model = Formulario
        #especifica los campos del modelo que se van a incluir en el formulario 
        fields = ['nombre', 'apellido', 'telefono', 'correo']

