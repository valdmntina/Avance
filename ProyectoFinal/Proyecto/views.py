from django.shortcuts import render
from django.http import HttpResponse
from .models import Serpientes
# Create your views here.

def index(request):
    return render(request, 'index.html')

def importancia(request):
    return render(request, 'importancia.html')

def historia(request):
    return render(request, 'historia.html')

# def ubicacion(request):
#     return render(request,'ubicacion.html')

def lista_serpientes(request):
    especies = Serpientes.objects.all()
    return render (request, 'ubicacion.html', {
        'especie': especies
    } )

def caracteristica_serpiente(request, serpiente_id):
    especie = Serpientes.objects.all(id=serpiente_id)
    return render(request, 'ubicacion.html', {
        'especie': especie
    })