from django.urls import path
from app.views import ContentAV,ArtistAV,StreamingPlatformAV
urlpatterns = [
    path('content-list/',ContentAV.as_view()),
    path('artist-list/',ArtistAV.as_view()),
    path('platforms-list/',StreamingPlatformAV.as_view()),
]
