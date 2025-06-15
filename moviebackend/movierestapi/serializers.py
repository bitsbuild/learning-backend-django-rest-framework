from rest_framework import serializers
from movierestapi.models import Movie
def name_length(value):
    if len(value)>50:
        raise serializers.ValidationError("Name Too Long! Restrict To 50 Characters")
    else:
        return value
def desc_length(value):
    if len(value)>250:
        raise serializers.ValidationError("Description Too Long! Restrict To 250 Characters")
    else:
        return value
class MovieSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField(validators=[desc_length])
    isReleased = serializers.BooleanField()
    reviews = serializers.JSONField()
    cast = serializers.JSONField()
    # BELOW FUNCTION: CREATE IS CALLED ON POST AND UPDATE IS CALLED ON PUT BY THE SERIALIZER
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