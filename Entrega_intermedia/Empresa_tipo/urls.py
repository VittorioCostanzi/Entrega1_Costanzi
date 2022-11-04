from django.urls import path
from .views import inicio, nosotros, proyectos, contacto

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('proyectos/', proyectos, name="Proyectos"),
    path('contacto/', contacto, name="Contacto"),
]