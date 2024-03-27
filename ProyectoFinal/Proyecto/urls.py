from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('importancia/', views.importancia, name='importancia'),
    path('historia/', views.historia, name='historia'),
    path('ubicacion/', views.lista_serpientes, name='lista_serpientes'),
    path('ubicacion/', views.caracteristica_serpiente, name='lista_serpientes'),
]   