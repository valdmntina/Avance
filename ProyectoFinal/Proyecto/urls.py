from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('importancia/', views.importancia, name='Importancia'),
    path('historia/', views.historia, name='Historia'),
    path('registrar_serpiente/<str:ncien>/<str:ncomu>/<str:h>/<str:d>', views.registrar_serpientes, name='registrar_serpientes'), #no usar de nuevo
    path('editar/', views.editar, name='editar'),
    path('registro_serpientes/', views.registro_serpientes, name='registro_serpientes'), #usar de nuevo solo si es necesario, comentar los que ya estan
    path('caracteristica_serpiente/', views.caracteristica_serpiente, name='caracteristica_serpiente'), #usar de nuevo solo si es necesario, comentar los que ya estan
    path('elimina/<int:id>', views.elimina, name='elimina'),
    path('ubicacion/', views.lista_serpientes, name='Lista_serpientes'),
    path('formulario/', views.formulario, name='Formulario'),
]   