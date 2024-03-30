from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('importancia/', views.importancia, name='Importancia'),
    path('historia/', views.historia, name='Historia'),
    path('registrar_serpiente/<str:ncien>/<str:ncomu>/<str:h>/<str:d>', views.registrar_serpientes, name='registrar_serpientes'),
    path('editar/', views.editar, name='editar'),
    path('registro_serpientes/', views.registro_serpientes, name='registro_serpientes')
    # path('ubicacion/', views.registrar_serpientes, name='lista_serpientes'),
    # path('ubicacion/', views.caracteristica_serpiente, name='lista_serpientes'),
]   