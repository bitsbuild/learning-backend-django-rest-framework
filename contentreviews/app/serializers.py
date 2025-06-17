from app.models import ContentDetails,StreamingPlatform,Artists,ContentReviews
from rest_framework import serializers
class ContentReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentReviews
        fields = '__all__'
        exclude = []
class ContentSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ContentReviewSerializer(many=True,read_only=True)
    class Meta:
        model = ContentDetails
        fields = '__all__'
        exclude = []
class StreamingPlatformSerializer(serializers.HyperlinkedModelSerializer):
    content = ContentSerializer(many=True,read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = '__all__'
        exclude = []
class ArtistsSerializer(serializers.HyperlinkedModelSerializer):
    content = ContentSerializer(many=True,read_only=True)
    class Meta:
        model = Artists
        fields = '__all__'
        exclude = []
