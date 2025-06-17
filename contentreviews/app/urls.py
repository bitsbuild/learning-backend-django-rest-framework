from django.urls import path
from app.views import ContentListCreateAV,ArtistListCreateAV,StreamingPlatformListCreateAV,ReviewsListCreateAV,ContentDetailAV,ArtistDetailAV,StreamingPlatformDetailAV,ReviewsDetailAV
urlpatterns = [
    path('content-list/',ContentListCreateAV.as_view()),
    path('content-update-delete/<uuid:pk>',ContentDetailAV.as_view()),
    path('artist-list/',ArtistListCreateAV.as_view()),
    path('artist-update-delete/<uuid:pk>',ArtistDetailAV.as_view()),
    path('platforms-list/',StreamingPlatformListCreateAV.as_view()),
    path('platform-update-delete/<uuid:pk>',StreamingPlatformDetailAV.as_view()),
    path('content-review/',ReviewsListCreateAV.as_view()),
    path('review-update-delete/<uuid:pk>',ReviewsDetailAV.as_view()),
]
