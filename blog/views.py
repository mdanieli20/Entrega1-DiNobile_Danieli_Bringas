from django.shortcuts import render, redirect
from .forms import FormNoticia, BusquedaNoticia
from .models import Noticia
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')


def crear_noticia(request):    
    if request.method == 'POST':
        form = FormNoticia(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now() 
            
            noticia = Noticia(
                titulo=data.get('titulo'),
                contenido=data.get('contenido'),
                fecha_creacion=fecha
            )
            noticia.save()

            return redirect('listado_noticias')
        
        else:
            return render(request, 'crear_noticia.html', {'form': form})
            
    
    form_noticia = FormNoticia()
    
    return render(request, 'crear_noticia.html', {'form': form_noticia})

def listado_noticias(request):
    
    nombre_de_busqueda = request.GET.get('titulo')
    
    if nombre_de_busqueda:
        listado_noticias = Noticia.objects.filter(titulo__icontains=nombre_de_busqueda) 
    else:
        listado_noticias = Noticia.objects.all()
    
    form = BusquedaNoticia()
    return render(request, 'listado_noticias.html', {'listado_noticias': listado_noticias, 'form': form})

def nosotros(request):
    return render(request, 'nosotros.html')