from django.shortcuts import render

# Create your views here.
def inicio(request):
    
    return render(request, "template_inicio.html")

def nosotros(request):
    
    return render(request, "template_nosotros.html")

def proyectos(request):
    
    return render(request, "template_proyectos.html")

def contacto(request):
    
    return render(request, "template_contacto.html")