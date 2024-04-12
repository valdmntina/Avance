from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name='index'),
    #menu importancia
    path('importancia/', views.importancia, name='Importancia'),
    #menu historuia
    path('historia/', views.historia, name='Historia'),
    #registré serpientes con url
    path('registrar_serpiente/<str:ncien>/<str:ncomu>/<str:h>/<str:d>', views.registrar_serpientes, name='registrar_serpientes'), #no usar de nuevo
    #edité un registro
    path('editar/', views.editar, name='editar'),
    #ingresé los datos a la base de datos
    path('registro_serpientes/', views.registro_serpientes, name='registro_serpientes'), #usar de nuevo solo si es necesario, comentar los que ya estan
    #ingresé los datos a la base de datos
    path('caracteristica_serpiente/', views.caracteristica_serpiente, name='caracteristica_serpiente'), #usar de nuevo solo si es necesario, comentar los que ya estan
    #eliminé registros repetidos mediante el id en la url
    path('elimina/<int:id>', views.elimina, name='elimina'),
    #menu ubicacion
    path('ubicacion/', views.lista_serpientes, name='Lista_serpientes'),
    path('info_serpiente/<int:id>', views.info_serpiente, name='info_serpiente'),
    #menu formulario
    path('formulario/', views.formulario, name='Formulario'),
    
]   