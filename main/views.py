from django.shortcuts import render
from .models import Movie, Comment
from .forms import UserForm
from django.shortcuts import redirect


def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie_recommendations = Movie.objects.filter(genre=movie.genre).exclude(id=movie_id)
    return render(request, 'details.html', {'movie': movie, 'movie_recommendations': movie_recommendations})

def watch(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'main.html', {'movie': movie})

def registration(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'registration.html', {'form': form})


def search(request):
    query = request.GET.get('query')
    movies = Movie.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'movies': movies})

def status_404(request):
    return render(request, '404.html',status=404)

def status_500(request):
    return render(request, '500.html',status=500)

def status_403(request):
    return render(request, '403.html',status=403)
import requests
from datetime import datetime
from django.core.management.base import BaseCommand
import random


def handle(self, *args, **kwargs):
        movie_od = random.randint(1, 100)
        LANGUAGE = [
            ('hi',
            'en'
            
            )]
        languages = random.choice(LANGUAGE)
        api_key = 'API_KEY'  # Replace with your TMDb API key
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language={languages}&page={movie_od}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['results']
            for movie_data in data:
                movie = Movie()
                movie.title = movie_data['title']
                movie.bio = movie_data['overview']
                movie.year = '2015'
                # movie.poster = movie_data['poster_path'] if movie_data['poster_path'] else None
                poster_base_url = 'https://image.tmdb.org/t/p/'
                poster_size = 'w500'  # Choose an appropriate size
                movie.poster = movie_data['poster_path']
                if movie.poster:
                    movie.poster = f"{poster_base_url}{poster_size}{movie.poster}"
                else:
                    movie.poster = None
                movie.logo = f"{poster_base_url}{poster_size}{movie_data['backdrop_path']}" if movie_data['backdrop_path'] else None
                movie.trailer = f'https://www.youtube.com/watch?v={movie_data["id"]}'
                movie.language = movie_data['original_language']
                movie.link = f'https://www.themoviedb.org/movie/{movie_data["id"]}'
                movie.genre = movie_data['genre_ids'][0] if movie_data['genre_ids'] else None
                movie.movie_rating = movie_data['vote_average']


                movie.save()
                return redirect('main:index')
        else:
            return redirect('main:index')

