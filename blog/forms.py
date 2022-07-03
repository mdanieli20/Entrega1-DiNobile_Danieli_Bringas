from django import forms

class FormNoticia(forms.Form):
    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=300)
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaNoticia(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)