from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria)
    lugar = models.CharField(max_length=100)
    inicio = models.DateTimeField()
    termino = models.DateTimeField()
    imagen = models.ImageField(upload_to = 'events')
    gratis = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    organizador = models.ForeignKey(User)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre