from django.contrib import admin
from .models import *

class FormularioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono')
    search_fields = ('nombre', 'telefono')
    list_filter = ('nombre', 'apellido')

# Register your models here.
admin.site.register(Serpientes)
admin.site.register(Caracteristica)
admin.site.register(Formulario, FormularioAdmin)