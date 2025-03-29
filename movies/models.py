from django.db import models
from django.views.generic import DetailView

# Create your models here.
from django.db import models

class Pelicula(models.Model):
    # Choices for genre
    GENERO_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Biography', 'Biography'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Science Fiction'),
        ('Thriller', 'Thriller'),
    ]

class Pelicula(models.Model):
    imagen = models.ImageField(upload_to='Peliculas')
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    descripcion = models.TextField
    trailer = models.URLField(max_length=200)

class MovieDetailView(DetailView):
    model = Pelicula
    template_name = 'movies/movie.detail.html'