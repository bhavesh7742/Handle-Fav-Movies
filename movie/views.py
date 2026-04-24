from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Movie
from .forms import MovieForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'movie/index.html')


def movie_list(request):
    if request.user.is_authenticated:
        movies = Movie.objects.filter(user=request.user).order_by('-created_at')
    else:
        movies = Movie.objects.none()
    return render(request, 'movie/movie_list.html', {'movies': movies})


@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, files=request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie/movie_form.html', {'form': form})


@login_required
def movie_edit(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if movie.user != request.user:
        return HttpResponseForbidden("You can only edit your own movies.")
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie/movie_form.html', {'form': form})


@login_required
def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie.user != request.user:
        return HttpResponseForbidden("You can only delete your own movies.")
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movie/movie_confirm_delete.html', {'movie': movie})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})