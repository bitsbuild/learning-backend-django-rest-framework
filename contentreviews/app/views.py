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
        serialized_contents = ContentSerializer(contents,many=True, context={'request': request})
        return Response(serialized_contents.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=ContentSerializer)
    def post(self,request):
        new_content = ContentSerializer(data=request.data, context={'request': request})
        if new_content.is_valid():
            new_content.save()
            return Response(new_content.data,status=status.HTTP_200_OK)
        else:
            return Response(new_content.errors,status=status.HTTP_400_BAD_REQUEST)
class ContentDeleteUpdateAV(APIView):
    def delete(self,request,id):
        try:
            ContentDetails.objects.get(pk=id).delete()
            return Response({"status":"success"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"failure","error_message":str(e)},status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(request_body=ContentSerializer)
    def put(self,request,id):
        instance = ContentDetails.objects.get(pk=id)
        put_serializer = ContentSerializer(instance,data=request.data, context={'request': request})
        if put_serializer.is_valid():
            put_serializer.save()
            return Response(put_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(put_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ArtistAV(APIView):
    def get(self,request):
        artists = Artists.objects.all()
        serialized_artists = ArtistsSerializer(artists,many=True, context={'request': request})
        return Response(serialized_artists.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=ArtistsSerializer)
    def post(self,request):
        serialized_artist = ArtistsSerializer(data=request.data, context={'request': request})
        if serialized_artist.is_valid():
            serialized_artist.save()
            return Response(serialized_artist.data,status=status.HTTP_200_OK)
        else:
            return Response(serialized_artist.errors,status=status.HTTP_400_BAD_REQUEST)
class ArtistDeleteUpdateAV(APIView):
    def delete(self, request, id):
        try:
            Artists.objects.get(pk=id).delete()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "failure", "error_message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(request_body=ArtistsSerializer)
    def put(self, request, id):
        instance = Artists.objects.get(pk=id)
        put_serializer = ArtistsSerializer(instance, data=request.data, context={'request': request})
        if put_serializer.is_valid():
            put_serializer.save()
            return Response(put_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(put_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class StreamingPlatformAV(APIView):
    def get(self,request):
        platforms = StreamingPlatform.objects.all()
        serialized_platforms = StreamingPlatformSerializer(platforms,many=True, context={'request': request})
        return Response(serialized_platforms.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=StreamingPlatformSerializer)
    def post(self,request):
        new_platform = StreamingPlatformSerializer(data=request.data, context={'request': request})
        if new_platform.is_valid():
            new_platform.save()
            return Response(new_platform.data,status=status.HTTP_200_OK)
        else:
            return Response(new_platform.errors,status=status.HTTP_400_BAD_REQUEST)
class StreamingPlatformDeleteUpdateAV(APIView):
    def delete(self, request, id):
        try:
            StreamingPlatform.objects.get(pk=id).delete()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "failure", "error_message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(request_body=StreamingPlatformSerializer)
    def put(self, request, id):
        instance = StreamingPlatform.objects.get(pk=id)
        put_serializer = StreamingPlatformSerializer(instance, data=request.data, context={'request': request})
        if put_serializer.is_valid():
            put_serializer.save()
            return Response(put_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(put_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ContentReviewAV(APIView):
    def get(self,request):
        reviews = ContentReviews.objects.all()
        serialized_reviews = ContentReviewSerializer(reviews,many=True,context={'request': request})
        return Response(serialized_reviews.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=ContentReviewSerializer)
    def post(self,request):
        new_review = ContentReviewSerializer(data=request.data,context={'request': request})
        if new_review.is_valid():
            new_review.save()
            return Response(new_review.data,status=status.HTTP_200_OK)
        else:
            return Response(new_review.errors,status=status.HTTP_400_BAD_REQUEST)
class ContentReviewDeleteUpdateAV(APIView):
    def delete(self, request, id):
        try:
            ContentReviews.objects.get(pk=id).delete()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "failure", "error_message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(request_body=ContentReviewSerializer)
    def put(self, request, id):
        instance = ContentReviews.objects.get(pk=id)
        put_serializer = ContentReviewSerializer(instance, data=request.data,context={'request': request})
        if put_serializer.is_valid():
            put_serializer.save()
            return Response(put_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(put_serializer.errors, status=status.HTTP_400_BAD_REQUEST)