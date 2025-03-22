from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    generos = models.ManyToManyField('Genero')
    actores = models.ManyToManyField('Actor')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)
    puntuacion_imdb = models.FloatField(null=True, blank=True)
    trailer_youtube = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Actor(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre