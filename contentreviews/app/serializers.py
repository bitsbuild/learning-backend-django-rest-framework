from app.models import ContentDetails,StreamingPlatform,Artists,ContentReviews
from rest_framework import serializers
class ContentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentReviews
        fields = '__all__'
class ContentSerializer(serializers.ModelSerializer):
    reviews = ContentReviewSerializer(many=True,read_only=True)
    class Meta:
        model = ContentDetails
        fields = '__all__'
class StreamingPlatformSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True,read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = '__all__'
class ArtistsSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True,read_only=True)
    class Meta:
        model = Artists
        fields = '__all__'