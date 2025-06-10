from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from movierestapi.models import Movie
from movierestapi.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
def sample_function(request):
    return HttpResponse("Sample Function Working Very Well")
@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serialized_movies_list = MovieSerializer(movies,many=True)
    return Response(serialized_movies_list.data)
@api_view(['GET'])
def get_movie_detail(request,movie_name):
    movie_detail = Movie.objects.get(pk=movie_name) 
    serialized_movie_detail = MovieSerializer(movie_detail)
    return Response(serialized_movie_detail.data)