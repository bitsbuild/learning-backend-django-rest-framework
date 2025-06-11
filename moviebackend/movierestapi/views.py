from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from movierestapi.models import Movie
from movierestapi.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
def sample_function(request):
    return HttpResponse("Sample Function Working Very Well")
@api_view(['GET','POST'])
def movies(request):
    if request.method == 'GET':    
        movies = Movie.objects.all()
        serialized_movies_list = MovieSerializer(movies,many=True)
        return Response(serialized_movies_list.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
@api_view(['GET','PUT','DELETE'])
def movie_detail(request,id):
    if request.method == 'GET':
        movie_detail = Movie.objects.get(pk=id) 
        serialized_movie_detail = MovieSerializer(movie_detail)
        return Response(serialized_movie_detail.data)
    elif request.method == 'PUT':
        movie_detail = Movie.objects.get(pk=id) 
        serializer = MovieSerializer(movie_detail,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'DELETE':
        try:
            Movie.objects.get(pk=id).delete()
            return Response({"status":"success"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':str(e)},status=status.HTTP_400_BAD_REQUEST)