from django.urls import path
from movierestapi.views import sample_function,movies,movie_detail
urlpatterns = [
    path('sample/',sample_function),
    path('movies/',movies),
    path('movie-detail/<str:movie_name>',movie_detail),
]
