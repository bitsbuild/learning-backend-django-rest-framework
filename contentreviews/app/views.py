from rest_framework import generics
from app.models import ContentDetails, ContentReviews, Artists, StreamingPlatform
from app.serializers import ContentSerializer,ContentReviewSerializer,ArtistsSerializer,StreamingPlatformSerializer
class ContentListCreateAV(generics.ListCreateAPIView):
    queryset = ContentDetails.objects.all()
    serializer_class = ContentSerializer
class ContentDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentDetails.objects.all()
    serializer_class = ContentSerializer
class ArtistListCreateAV(generics.ListCreateAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
class ArtistDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
class StreamingPlatformListCreateAV(generics.ListCreateAPIView):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
class StreamingPlatformDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
class ReviewsListCreateAV(generics.ListCreateAPIView):
    queryset = ContentReviews.objects.all()
    serializer_class = ContentReviewSerializer
class ReviewsDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentReviews.objects.all()
    serializer_class = ContentReviewSerializer
class ContentPerPlatformAV(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        platform_id = self.kwargs['pk']
        return ContentDetails.objects.filter(content_platform=platform_id)
class ContentPerArtistAV(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        artist_id = self.kwargs['pk']
        return ContentDetails.objects.filter(artists__artist_id=artist_id)
