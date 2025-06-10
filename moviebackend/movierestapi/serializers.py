from rest_framework import serializers
class MovieSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    isReleased = serializers.BooleanField()
    reviews = serializers.JSONField()
    cast = serializers.JSONField()
