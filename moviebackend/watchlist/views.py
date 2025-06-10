from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from watchlist.models import Movie
# Create your views here.
def list_movie(request):
    movies = list(Movie.objects.all().values())
    data = {'Movies':movies}
    return JsonResponse(data)

def get_movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    return JsonResponse(dict({
        'name':movie.name,
        'desc':movie.description,
        'Released?':movie.isReleased
    }))