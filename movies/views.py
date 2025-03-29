from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Pelicula

# Create your views here.
class MovieListView(ListView):

    model= Pelicula 
    template_name= 'Movies/movie_list.html'

class MovieDetailView(DetailView):
    model = Pelicula
    template_name = 'Movies/movie.detail.html'