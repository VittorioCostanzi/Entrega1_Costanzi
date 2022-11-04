from django.shortcuts import render
from .forms import Formulario_contacto
from .models import Datos

# Create your views here.
def inicio(request):
    
    return render(request, "template_inicio.html")

def nosotros(request):
    
    return render(request, "template_nosotros.html")

def proyectos(request):
    
    return render(request, "template_proyectos.html")

def contacto(request):
    
    if request.method == "POST":

        miFormulario = Formulario_contacto(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                datos = Datos(nombre =informacion["nombre"],apellido = informacion["apellido"],consulta = informacion["consulta"])
                datos.save()
                return render(request, "template_inicio.html")
    else:
        miFormulario = Formulario_contacto()

    return render(request, "template_contacto.html", {"miFormulario": miFormulario})