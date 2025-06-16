from app.models import ContentDetails,StreamingPlatform,Artists,ContentReviews
from rest_framework import serializers
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        feilds = '__all__'
        exclude = []
class StreamingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        feilds = '__all__'
        exclude = []
class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        feilds = '__all__'
        exclude = []
class ContentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentReviews
        feilds = '__all__'
        exclude = []