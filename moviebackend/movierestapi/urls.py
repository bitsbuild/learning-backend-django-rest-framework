from django.urls import path
from movierestapi.views import MoviesAV,MovieDetailAV
urlpatterns = [
    path('movies/',MoviesAV.as_view()),
    path('movie-detail/<uuid:id>',MovieDetailAV.as_view()),
]
