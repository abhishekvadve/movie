from django.shortcuts import render
from .models import Movie, Comment
from .forms import UserForm
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

