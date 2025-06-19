from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from app.models import ContentDetails, ContentReviews, Artists, StreamingPlatform
from app.serializers import ContentSerializer,ContentReviewSerializer,ArtistsSerializer,StreamingPlatformSerializer
from app.permissions import AdminOrReadOnly,ReviewPermissions
class ContentViewSet(viewsets.ModelViewSet):
    queryset = ContentDetails.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['artists','content_platform']
    permission_classes=[AdminOrReadOnly]
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
    permission_classes=[AdminOrReadOnly]
class PlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
    permission_classes=[AdminOrReadOnly]
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ContentReviews.objects.all()
    serializer_class = ContentReviewSerializer
    permission_classes = [ReviewPermissions]
    def perform_create(self, serializer):
        serializer.save(review_user=self.request.user)