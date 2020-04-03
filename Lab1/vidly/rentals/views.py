from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Movie
from .models import Game

### CRUD
#from .models import Movie

# Movie.objects.all()

# Movie.objects.filter(release_year=2001)

# Movie.objects.get(id=1)

# def index(request):
    # movies = Movie.objects.all()
    # return render(request, 'views/index.html', { 'movies': movies } )





""" def index(request):
    my_dict = {"insert_me": "I am from views.py", "Josh": "My first name is Josh.", "List": "Animal Crossing, Homework, Exercise, and Sleep."}
    return render(request, 'views/index.html', context=my_dict)


     """

def index(request):
    movies = Movie.objects.all()
    return render(request, 'views/index.html', { 'movies': movies } )

def cart(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.in_stock -= 1
    movie.save()
    return render(request,'views/cart.html', { 'movie': movie } )

