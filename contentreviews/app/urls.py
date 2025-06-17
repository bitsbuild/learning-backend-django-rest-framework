from django.urls import path
from app.views import (ContentListCreateAV,
                       ArtistListCreateAV,
                       StreamingPlatformListCreateAV,
                       ReviewsListCreateAV,
                       ContentDetailAV,
                       ArtistDetailAV,
                       StreamingPlatformDetailAV,
                       ReviewsDetailAV,
                       ContentPerPlatformAV,
                       ContentPerArtistAV,)
urlpatterns = [
    path('content/',ContentListCreateAV.as_view()),

    path('content/<uuid:pk>/',ContentDetailAV.as_view()),

    path('artist/',ArtistListCreateAV.as_view()),

    path('artist/<uuid:pk>/',ArtistDetailAV.as_view()),

    path('platform/',StreamingPlatformListCreateAV.as_view()),

    path('platform/<uuid:pk>/',StreamingPlatformDetailAV.as_view()),

    path('review/',ReviewsListCreateAV.as_view()),

    path('review/<uuid:pk>/',ReviewsDetailAV.as_view()),

    path('platform/<uuid:pk>/contents/',ContentPerPlatformAV.as_view()),
    
    path('artist/<uuid:pk>/contents/',ContentPerArtistAV.as_view()),
]
