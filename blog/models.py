from django.db import models
# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=300)
    fecha_creacion = models.DateField(null=True)