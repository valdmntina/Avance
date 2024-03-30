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

def registrar_serpientes(request, ncien, ncomu, h, d):
    nueva_serpiente = Serpientes(nombre_cientifico= ncien, nombre_comun=ncomu,
                                 habitat=h, descripcion=d)
    nueva_serpiente.save()
    return HttpResponse('Se registro exitosamente')

def editar(request):
    registro = Serpientes.objects.get(id=3)
    registro.habitat = 'Bosques tropicales y sabanas'
    registro.save()
    return HttpResponse('corregido')

def registro_serpientes(request):
    # serpiente4 = Serpientes.objects.create(nombre_cientifico='Pantherophis guttatus',
    #                                        nombre_comun='Serpiente de maíz',
    #                                        habitat='Campos agricolas y bosques',
    #                                        descripcion='Tamaño pequeño y docil')
    # serpiente4.save()
    serpiente5 = Serpientes.objects.create(nombre_cientifico='Uromacerinae',
                                           nombre_comun='Serpiente arborícola',
                                           habitat='Árboles de los bosques tropicales y subtropicales',
                                           descripcion='Inofensivas para los humanos')
    serpiente5.save()

    serpiente6 = Serpientes.objects.create(nombre_cientifico='Pseudoboa neuwiedii',
                                           nombre_comun='Serpiente ratonera común',
                                           habitat='Bosques hasta áreas agrícolas',
                                           descripcion='Su alimentación se basa en roedores y pequeños mamiferos')
    serpiente6.save()

    serpiente7 = Serpientes.objects.create(nombre_cientifico='Drymobius margaritiferus',
                                           nombre_comun='Serpiente corredora',
                                           habitat='Bosques',
                                           descripcion='Rápida velocidad y agilidad para moverse por el suelo y árboles')
    serpiente7.save()

    serpiente8 = Serpientes.objects.create(nombre_cientifico='Erythrolamprus bizona',
                                           nombre_comun='Serpiente falsa coral',
                                           habitat='Bosques tropicales y sabanas',
                                           descripcion='Apariencia similar a la serpiente coral, inofensiva para los humanos')
    serpiente8.save()
    return HttpResponse('Registradas :D')

#esto es para una vez ya tenga metidas las serpientes
# def lista_serpientes(request):
#     especies = Serpientes.objects.all()
#     return render (request, 'ubicacion.html', {
#         'especie': especies
#     } )

# def caracteristica_serpiente(request, serpiente_id):
#     especie = Serpientes.objects.all(id=serpiente_id)
#     return render(request, 'ubicacion.html', {
#         'especie': especie
#     })