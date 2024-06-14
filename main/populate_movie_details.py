import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from .models import Movie

class Command(BaseCommand):
    help = 'Populate Movie model with data from TMDb'

    def handle(self, *args, **kwargs):
        api_key = 'cd49c2d35af7855097ab97cbbdd70f2a'  # Replace with your TMDb API key
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['results']
            for movie_data in data:
                movie = Movie()
                movie.title = movie_data['title']
                movie.bio = movie_data['overview']
                movie.yeaer = datetime.strptime(movie_data['release_date'], '%Y').date()
                movie.poster = movie_data['poster_path'] if movie_data['poster_path'] else None
                movie.trailer = f'https://www.youtube.com/watch?v={movie_data["id"]}'
                movie.language = movie_data['original_language']
                movie.link = f'https://www.themoviedb.org/movie/{movie_data["id"]}'
                movie.genre = movie_data['genre_ids'][0] if movie_data['genre_ids'] else None
                movie.duration = f'{movie_data["runtime"]} minutes' if movie_data['runtime'] else None
                movie.movie_rating = movie_data['vote_average']


                movie.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added movie: {movie.title}'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from TMDb API'))
