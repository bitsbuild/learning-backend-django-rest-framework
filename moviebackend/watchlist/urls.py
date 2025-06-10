from django.urls import path
from watchlist.views import get_movie_details,list_movie

urlpatterns = [
    path('list/',list_movie),
    path('details/<int:pk>',get_movie_details)
]
