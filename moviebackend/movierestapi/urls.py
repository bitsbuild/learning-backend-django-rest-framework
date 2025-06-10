from django.urls import path
from movierestapi.views import sample_function,get_movies,get_movie_detail
urlpatterns = [
    path('sample/',sample_function),
    path('get-movies/',get_movies),
    path('get-movie-detail/<str:movie_name>',get_movie_detail)
]
