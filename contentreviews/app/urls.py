from django.urls import path
from app.views import ContentListCreateAV,ArtistListCreateAV,StreamingPlatformListCreateAV,ReviewsListCreateAV,ContentDetailAV,ArtistDetailAV,StreamingPlatformDetailAV,ReviewsDetailAV
urlpatterns = [
    path('content-list/',ContentListCreateAV.as_view()),
    path('content-update-delete/<uuid:id>',ContentDetailAV.as_view()),
    path('artist-list/',ArtistListCreateAV.as_view()),
    path('artist-update-delete/<uuid:id>',ArtistDetailAV.as_view()),
    path('platforms-list/',StreamingPlatformListCreateAV.as_view()),
    path('platform-update-delete/<uuid:id>',StreamingPlatformDetailAV.as_view()),
    path('content-review/',ReviewsListCreateAV.as_view()),
    path('review-update-delete/<uuid:id>',ReviewsDetailAV.as_view()),
]
