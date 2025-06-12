from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from movierestapi.models import Movie
from movierestapi.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
class MoviesAV(APIView):
    def get(self,request):
        try:
            mov = Movie.objects.all()
            serialized_mov = MovieSerializer(mov,many=True)
            return Response(serialized_mov.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serialized_mov.errors,status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        mov = MovieSerializer(data=request.data)
        if mov.is_valid():
            mov.save()
            return Response(mov.data,status=status.HTTP_200_OK)
        else:
            return Response(mov.errors,status=status.HTTP_400_BAD_REQUEST)
class MovieDetailAV(APIView):
    def get(self,request,id):
        try:
            movie = Movie.objects.get(pk=id)
            serialized_movie = MovieSerializer(movie)
            return Response(serialized_movie.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serialized_movie.error_messages,status=status.HTTP_404_NOT_FOUND)
    def put(self,request,id):
        movie = Movie.objects.get(pk=id)
        serrializer = MovieSerializer(movie,data=request.data)
        if serrializer.is_valid():
            serrializer.save()
            return Response(serrializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serrializer.error,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        try:
            Movie.objects.get(pk=id).delete()
            return Response({"status":"successful deletion"})
        except Exception as e:
            return Response({"status":"error","error":str(e)},status=status.HTTP_400_BAD_REQUEST)
# --------------------FUNCTION BASED VIEWS--------------------
# @api_view(['GET', 'POST'])
# def movies(request):
#     if request.method == 'GET':    
#         movies = Movie.objects.all()
#         serialized_movies_list = MovieSerializer(movies, many=True)
#         return Response(serialized_movies_list.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, id):
#     if request.method == 'GET':
#         try:
#             movie_detail = Movie.objects.get(pk=id) 
#             serialized_movie_detail = MovieSerializer(movie_detail)
#             return Response(serialized_movie_detail.data, status=status.HTTP_200_OK)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

#     elif request.method == 'PUT':
#         try:
#             movie_detail = Movie.objects.get(pk=id) 
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie_detail, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         try:
#             Movie.objects.get(pk=id).delete()
#             return Response({"status": "success"}, status=status.HTTP_200_OK)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)
