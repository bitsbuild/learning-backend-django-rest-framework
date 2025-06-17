from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from app.models import ContentDetails, ContentReviews, Artists, StreamingPlatform
from app.serializers import ContentSerializer, ContentReviewSerializer, ArtistsSerializer, StreamingPlatformSerializer
class ContentListCreateAV(generics.ListCreateAPIView):
    queryset = ContentDetails.objects.all()
    serializer_class = ContentSerializer
    @swagger_auto_schema(operation_summary="List all content items")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Create a new content item")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
class ContentDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentDetails.objects.all()
    serializer_class = ContentSerializer
    @swagger_auto_schema(operation_summary="Retrieve a specific content item")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Update a specific content item")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Delete a specific content item")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
class ArtistListCreateAV(generics.ListCreateAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
    @swagger_auto_schema(operation_summary="List all artists")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Create a new artist")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
class ArtistDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
    @swagger_auto_schema(operation_summary="Retrieve a specific artist")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Update a specific artist")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Delete a specific artist")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
class StreamingPlatformListCreateAV(generics.ListCreateAPIView):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
    @swagger_auto_schema(operation_summary="List all streaming platforms")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Create a new streaming platform")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
class StreamingPlatformDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
    @swagger_auto_schema(operation_summary="Retrieve a specific streaming platform")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Update a specific streaming platform")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Delete a specific streaming platform")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
class ReviewsListCreateAV(generics.ListCreateAPIView):
    queryset = ContentReviews.objects.all()
    serializer_class = ContentReviewSerializer
    @swagger_auto_schema(operation_summary="List all content reviews")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Create a new content review")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
class ReviewsDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentReviews.objects.all()
    serializer_class = ContentReviewSerializer
    @swagger_auto_schema(operation_summary="Retrieve a specific review")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Update a specific review")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Delete a specific review")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)