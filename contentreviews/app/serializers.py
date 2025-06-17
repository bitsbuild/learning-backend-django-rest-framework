from app.models import ContentDetails,StreamingPlatform,Artists,ContentReviews
from rest_framework import serializers
class ContentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentReviews
        feilds = '__all__'
        exclude = []
class ContentSerializer(serializers.ModelSerializer):
    reviews = ContentReviewSerializer(many=True,read_only=True)
    class Meta:
        model = ContentDetails
        feilds = '__all__'
        exclude = []
class StreamingPlatformSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True,read_only=True)
    class Meta:
        model = StreamingPlatform
        feilds = '__all__'
        exclude = []
class ArtistsSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True,read_only=True)
    class Meta:
        model = Artists
        feilds = '__all__'
        exclude = []
