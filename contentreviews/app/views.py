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
    @swagger_auto_schema(request_body=ContentDetails)
    def post(self,request):
        new_content = ContentSerializer(data=request.data)
        if new_content.is_valid():
            new_content.save()
            return Response(new_content.data,status=status.HTTP_200_OK)
        else:
            return Response(new_content.data,status=status.HTTP_400_BAD_REQUEST)
class ArtistAV(APIView):
    def get(self,request):
        pass
    @swagger_auto_schema(request_body=Artists)
    def post(self,request):
        pass
class StreamingPlatformAV(APIView):
    def get(self,request):
        pass
    @swagger_auto_schema(request_body=StreamingPlatform)
    def post(self,request):
        pass
class ContentReviewAV(APIView):
    def get(self,request):
        pass
    @swagger_auto_schema(request_body=ContentReviews)
    def post(self,request):
        pass