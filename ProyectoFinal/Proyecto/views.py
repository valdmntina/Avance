from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Serpientes, Caracteristica, Formulario
from .forms import Form

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

def registro_serpientes(request): #ya use todo esto, no usar de nuevo a no ser que sea necesario, comentar los que ya estan
    # INOFENSIVAS
    serpiente4 = Serpientes.objects.create(nombre_cientifico='Pantherophis guttatus',
                                           nombre_comun='Serpiente de maíz',
                                           habitat='Campos agricolas y bosques',
                                           descripcion='Tamaño pequeño y docil')
    serpiente4.save()
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

    serpiente9 = Serpientes.objects.create(nombre_cientifico='Drepanoides anomalus',
                                           nombre_comun='Serpiente de liga',
                                           habitat='Áreas boscosas',
                                           descripcion='Inofensiva para los humanos')
    serpiente9.save()

    serpiente10 = Serpientes.objects.create(nombre_cientifico='Chironius monticola',
                                            nombre_comun='Serpiente látigo colombiana',
                                            habitat='Bosques y áreas arbustivas',
                                            descripcion='Conocida por su cuerpo largo y delgado')
    serpiente10.save()

    serpiente11 = Serpientes.objects.create(nombre_cientifico='Pseustes poecilonotus',
                                            nombre_comun='Serpiente maicera',
                                            habitat='Variada',
                                            descripcion='Conocida tambien como serpiente maicera rayada')
    serpiente11.save()

    serpiente12 = Serpientes.objects.create(nombre_cientifico='Helicops angulatus',
                                            nombre_comun='Serpiente de agua colombiana',
                                            habitat='Ríos, lagos y pantanos',
                                            descripcion='Encontrada comúnmente en lugares acuáticos')
    serpiente12.save() 

    # VENENOSAS

    serpiente13 = Serpientes.objects.create(nombre_cientifico='Bothrops asper',
                                            nombre_comun='Terciopelo o Barba amarilla',
                                            habitat='Variada',
                                            descripcion='Coloracion variada con patrones')
    serpiente13.save()

    serpiente14 = Serpientes.objects.create(nombre_cientifico='Bothrops atrox',
                                            nombre_comun='Jergón',
                                            habitat='Selvas y bosques tropicales humedos',
                                            descripcion='Cuerpo grueso y cabeza triangular')
    serpiente14.save()

    serpiente15 = Serpientes.objects.create(nombre_cientifico='Lachesis muta',
                                            nombre_comun='Serpiente de cascabel muda',
                                            habitat='Selvas y bosques tropicales densos',
                                            descripcion='Cuerpo grueso con cabeza grande y triangular')
    serpiente15.save()

    serpiente16 = Serpientes.objects.create(nombre_cientifico='Micrurus spp',
                                            nombre_comun='Serpiente coralillo',
                                            habitat='Selvas, bosques secos, sabanas y zonas semiáridas',
                                            descripcion='Confundidas con serpientes no venenosas')
    serpiente16.save()
    return HttpResponse('Registradassss :DD')

def caracteristica_serpiente(request): #ya use todo esto, no usar de nuevo a no ser que sea necesario, comentar los que ya estan
    serpiente1 = Serpientes.objects.get(id=1)
    caracteristicas = Caracteristica.objects.create(venenosa=False,
                                                    color_patron='No tiene un patron especifico, pero sus colores le ayudan a camuflarse',
                                                    alimentacion='Mamiferos pequeños, aves y reptiles (de vez en cuando)',
                                                    serpiente_id=serpiente1.id)
    
    caracteristicas.save()

    serpiente2 = Serpientes.objects.get(id=2)
    caracteristicas2 = Caracteristica.objects.create(venenosa=False,
                                                     color_patron='No tiene un patron especifico, su color de fondo suele ser verde o marrón y le ayuda a camuflarse',
                                                     alimentacion='Varia según la disponibilidad de presa, comunmente mamiferos, aves, reptiles o peces',
                                                     serpiente_id=serpiente2.id)
    caracteristicas2.save()

    serpiente3 = Serpientes.objects.get(id=3)
    caracteristicas3 = Caracteristica.objects.create(venenosa=False,
                                                     color_patron='Anillos o bandas rojas y negras',
                                                     alimentacion='Animales pequeños y sus huevos',
                                                     serpiente_id=serpiente3.id)
    caracteristicas3.save()

    serpiente4 = Serpientes.objects.get(id=4)
    caracteristicas4 = Caracteristica.objects.create(venenosa=False,
                                                     color_patron='Color amarillo, anaranjado o marron con manchas rojas, naranjas, marrón oscuro o negro',
                                                     alimentacion='Mamiferos pequeños y otros reptiles pequeños',
                                                     serpiente_id=serpiente4.id)
    caracteristicas4.save()

    serpiente5 = Serpientes.objects.get(id=5)
    caracteristicas5 = Caracteristica.objects.create(venenosa=False,
                                                     color_patron='Color verde o marrón',
                                                     alimentacion='Depende de su habitat',
                                                     serpiente_id=serpiente5.id)
    caracteristicas5.save()

    serpiente6 = Serpientes.objects.get(id=6)
    caracteristicas6 = Caracteristica.objects.create(venenosa=False,
                                                     color_patron='Varia según la especie, su fondo suele ser marron o gris con manchas o rayas negras, marrones o rojizas',
                                                     alimentacion='Pequeños mamiferos, aves pequeñas y otros reptiles',
                                                     serpiente_id=serpiente6.id)
    caracteristicas6.save()

    serpiente7 = Serpientes.objects.get(id=7)
    caracteristicas7 =  Caracteristica.objects.create(venenosa=False,
                                                      color_patron='Varia según la subespecie y region donde se encuentre, su color suele ser marrón, gris o verde oliva con manchas o rayas',
                                                      alimentacion='Varia según el habitat, comunmente mamiferos pequeños y otros reptiles pequeños',
                                                      serpiente_id=serpiente7.id)
    caracteristicas7.save()

    serpiente8 = Serpientes.objects.get(id=8)
    caracteristicas8 = Caracteristica.objects.create(venenosa=False,
                                                     color_patron='Bandas negras anchas separadas por bandas de color rojo, anaranjado o marrón',
                                                     alimentacion='Pequeños vertebrados y ocacionalemente otras serpientes',
                                                     serpiente_id=serpiente8.id)
    caracteristicas8.save()

    serpiente9 = Serpientes.objects.get(id=9)
    caracteristicas9 = Caracteristica.objects.create(venenosa=False,
                                                     color_patron='Fondo rojo con bandas marrón oscuro y blancas',
                                                     alimentacion='Pequeños mamiferos',
                                                     serpiente_id=serpiente9.id)
    caracteristicas9.save()

    serpiente10 = Serpientes.objects.get(id=10)
    caracteristicas10 = Caracteristica.objects.create(venenosa=False,
                                                      color_patron='Fondo verde o verde oliva con bandas negras',
                                                      alimentacion='Pequeños mamiferos y ocasionalmente insectos',
                                                      serpiente_id=serpiente10.id)
    caracteristicas10.save()

    serpiente11 = Serpientes.objects.get(id=11)
    caracteristicas11 = Caracteristica.objects.create(venenosa=False,
                                                      color_patron='Fondo marrón o grisáceo con bandas oscuras',
                                                      alimentacion='Aves y pequeños mamiferos',
                                                      serpiente_id=serpiente11.id)
    caracteristicas11.save()

    serpiente12 = Serpientes.objects.get(id=12)
    caracteristicas12 = Caracteristica.objects.create(venenosa=False,
                                                      color_patron='Dorso marrón y vientre color crema o amarillento',
                                                      alimentacion='Animales acuáticos y ocasionalmente mamiferos que habitan cerca o en los cuerpos de agua donde habitan',
                                                      serpiente_id=serpiente12.id)
    caracteristicas12.save()

    serpiente13 = Serpientes.objects.get(id=13)
    caracteristicas13 = Caracteristica.objects.create(venenosa=True,
                                                      color_patron='Fondo marrón o grisáceo con bandas oscuras, sus bandas pueden variar',
                                                      alimentacion='Pequeños mamiferos y otros reptiles',
                                                      serpiente_id=serpiente13.id)
    caracteristicas13.save()

    serpiente14 = Serpientes.objects.get(id=14)
    caracteristicas14 = Caracteristica.objects.create(venenosa=True,
                                                      color_patron='Variable, fondo marrón, grisáceo o beige con bandas marrón oscuro, negro o rojizo',
                                                      alimentacion='Pequeños mamiferos y otros reptiles',
                                                      serpiente_id=serpiente14.id)
    caracteristicas14.save()

    serpiente15 = Serpientes.objects.get(id=15)
    caracteristicas15 = Caracteristica.objects.create(venenosa=True,
                                                      color_patron='Fondo marrón oscuro o negro con bandas marrón rojizo, naranja, amarrillo o crema',
                                                      alimentacion='Mamiferos pequeños y grandes',
                                                      serpiente_id=serpiente15.id)
    caracteristicas15.save()

    serpiente16 = Serpientes.objects.get(id=16)
    caracteristicas16 = Caracteristica.objects.create(venenosa=True,
                                                      color_patron='Bandas con colores brillantes como rojo, amarillo y negro',
                                                      alimentacion='Pequeños reptiles, anfibios y mamiferos pequeños',
                                                      serpiente_id=serpiente16.id)
    caracteristicas16.save()
    return HttpResponse('Se registro exitosamente')
    
    
def elimina(request, id):
    caracteristica = Caracteristica.objects.get(id=id)
    caracteristica.delete()
    return HttpResponse('Se eliminaron los repetidos')


def lista_serpientes(request):
    especies = Serpientes.objects.all()
    return render (request, 'ubicacion.html', {
        'especie': especies
    } )


def info_serpiente(request, id):
    serpiente = Serpientes.objects.get(id=id)
    return render(request, "info_serpiente.html", {
        'serpiente': serpiente
    })

def formulario(request):
    if request.method == 'POST':
      form = Form(request.POST)
      if form.is_valid():
          form.save()         
    else:
        form =Form()
    return render(request, 'formulario.html',{
        'formulario': form})

def elimina_formulario(request, id):
    formulario = Formulario.objects.get(id=id)
    formulario.delete()
    return HttpResponse('Eliminados exitosamente')
