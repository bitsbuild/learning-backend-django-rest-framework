from rest_framework import viewsets,generics
from app.models import ContentDetails, ContentReviews, Artists, StreamingPlatform
from app.serializers import ContentSerializer,ContentReviewSerializer,ArtistsSerializer,StreamingPlatformSerializer
class ContentViewSet(viewsets.ModelViewSet):
    queryset = ContentDetails.objects.all()
    serializer_class = ContentSerializer
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
class PlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ContentReviews.objects.all()
    serializer_class = ContentReviewSerializer

