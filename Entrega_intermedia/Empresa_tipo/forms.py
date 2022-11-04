from django import forms

class Formulario_contacto(forms.Form):
    nombre = forms.CharField(max_length = 30)
    apellido = forms.CharField(max_length = 30)
    consulta = forms.CharField(max_length = 300)