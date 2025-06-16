from django.urls import path
from app.views import ContentAV,ArtistAV
urlpatterns = [
    path('content-list/',ContentAV.as_view()),
    path('artist-list/',ArtistAV.as_view()),
]
