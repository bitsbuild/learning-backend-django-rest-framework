from app.models import ContentDetails,StreamingPlatform,Artists,ContentReviews
from rest_framework import serializers
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        feilds = '__all__'
class StreamingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        feilds = '__all__'
class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        feilds = '__all__'
class ContentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        feilds = '__all__'