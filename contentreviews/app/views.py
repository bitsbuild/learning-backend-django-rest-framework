from django.shortcuts import render
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from app.models import ContentDetails,ContentReviews,Artists,StreamingPlatform
from app.serializers import ContentSerializer,ContentReviewSerializer,ArtistsSerializer,StreamingPlatformSerializer
from rest_framework.response import Response
from rest_framework import status
class ContentAV(APIView):
    def get(self,request):
        contents = ContentDetails.objects.all()
        serialized_contents = ContentSerializer(contents,many=True)
        return Response(serialized_contents.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=ContentSerializer)
    def post(self,request):
        new_content = ContentSerializer(data=request.data)
        if new_content.is_valid():
            new_content.save()
            return Response(new_content.data,status=status.HTTP_200_OK)
        else:
            return Response(new_content.data,status=status.HTTP_400_BAD_REQUEST)
class ArtistAV(APIView):
    def get(self,request):
        artists = Artists.objects.all()
        serialized_artists = ArtistsSerializer(artists,many=True)
        return Response(serialized_artists.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=ArtistsSerializer)
    def post(self,request):
        serialized_artist = ArtistsSerializer(data=request.data)
        if serialized_artist.is_valid():
            serialized_artist.save()
            return Response(serialized_artist.data,status=status.HTTP_200_OK)
        else:
            return Response(serialized_artist.errors,status=status.HTTP_400_BAD_REQUEST)
class StreamingPlatformAV(APIView):
    def get(self,request):
        platforms = StreamingPlatform.objects.all()
        serialized_platforms = StreamingPlatformSerializer(platforms,many=True)
        return Response(serialized_platforms.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=StreamingPlatformSerializer)
    def post(self,request):
        new_platform = StreamingPlatformSerializer(data=request.data)
        if new_platform.is_valid():
            new_platform.save()
            return Response(new_platform.data,status=status.HTTP_200_OK)
        else:
            return Response(new_platform.errors,status=status.HTTP_400_BAD_REQUEST)
class ContentReviewAV(APIView):
    def get(self,request):
        pass
    @swagger_auto_schema(request_body=ContentReviewSerializer)
    def post(self,request):
        pass