from django.urls import path
from .views import index, crear_noticia, listado_noticias, nosotros

urlpatterns = [
    path('', index, name='index'),
    path('noticias/', listado_noticias, name='listado_noticias'),
    path('crear-noticia/', crear_noticia, name='crear_noticia'),
    path('nosotros/', nosotros, name='nosotros')
]