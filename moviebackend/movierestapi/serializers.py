from rest_framework import serializers

from movierestapi.models import Movie
class MovieSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    isReleased = serializers.BooleanField()
    reviews = serializers.JSONField()
    cast = serializers.JSONField()
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.isReleased = validated_data.get('isReleased',instance.isReleased)
        instance.reviews = validated_data.get('reviews',instance.reviews)
        instance.cast = validated_data.get('cast',instance.cast)
        instance.save()
        return instance