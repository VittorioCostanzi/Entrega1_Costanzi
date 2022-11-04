from django.urls import path
from .views import inicio, nosotros, proyectos, contacto

urlpatterns = [
    path('inicio/', inicio),
    path('nosotros/', nosotros),
    path('proyectos/', proyectos),
    path('contacto/', contacto),
]