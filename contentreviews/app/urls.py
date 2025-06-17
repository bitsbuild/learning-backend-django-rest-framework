from django.urls import path
from app.views import ContentListCreateAV,ArtistListCreateAV,StreamingPlatformListCreateAV,ReviewsListCreateAV,ContentDetailAV,ArtistDetailAV,StreamingPlatformDetailAV,ReviewsDetailAV
urlpatterns = [
    path('content/',ContentListCreateAV.as_view()),
    path('content/<uuid:pk>/',ContentDetailAV.as_view()),
    path('artist/',ArtistListCreateAV.as_view()),
    path('artist/<uuid:pk>/',ArtistDetailAV.as_view()),
    path('platforms/',StreamingPlatformListCreateAV.as_view()),
    path('platform/<uuid:pk>/',StreamingPlatformDetailAV.as_view()),
    path('review/',ReviewsListCreateAV.as_view()),
    path('review/<uuid:pk>/',ReviewsDetailAV.as_view()),
]
