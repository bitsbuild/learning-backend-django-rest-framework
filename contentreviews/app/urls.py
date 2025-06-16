from django.urls import path
from app.views import ContentAV,ArtistAV,StreamingPlatformAV,ContentReviewAV,ContentDeleteUpdateAV,ArtistDeleteUpdateAV,StreamingPlatformDeleteUpdateAV,ContentReviewDeleteUpdateAV
urlpatterns = [
    path('content-list/',ContentAV.as_view()),
    path('content-update-delete/<uuid:id>',ContentDeleteUpdateAV.as_view()),
    path('artist-list/',ArtistAV.as_view()),
    path('artist-update-delete/<uuid:id>',ArtistDeleteUpdateAV.as_view()),
    path('platforms-list/',StreamingPlatformAV.as_view()),
    path('platform-update-delete/<uuid:id>',StreamingPlatformDeleteUpdateAV.as_view()),
    path('content-review/',ContentReviewAV.as_view()),
    path('review-update-delete/<uuid:id>',ContentReviewDeleteUpdateAV.as_view()),
]
