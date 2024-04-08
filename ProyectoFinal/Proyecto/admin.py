from django.contrib import admin
from .models import *

class FormularioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo')
    search_fields = ('nombre', 'correo')
    list_filter = ('nombre', 'apellido')

# Register your models here.
admin.site.register(Serpientes)
admin.site.register(Caracteristica)
admin.site.register(Formulario, FormularioAdmin)