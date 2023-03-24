from django.shortcuts import render, redirect
from .models import Movies
from .forms import MovieForm
# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context={'movies':movies}
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            director = form.cleaned_data['director']
            comment = form.cleaned_data['comment']
            movie = Movies(title=title, director=director, comment=comment)
            movie.save()
            return redirect('movies:detail', movie.pk)
    form = MovieForm()
    context={'form':form}
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movies.objects.get(pk=pk)
    context={'movie':movie}
    return render(request, 'movies/detail.html', context)