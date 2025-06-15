from rest_framework import serializers
from movierestapi.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        feilds = ['name','description','isReleased','reviews','cast']
        
    def validate_name(self,value):
        if type(value) != str:
            raise serializers.ValidationError("String Movie Names Only")
        elif len(value)>50:
            raise serializers.ValidationError("Name Is Too Long, Restrict To 50 Characters")
        else:
            return value
        
    def validate_description(self,value):
        if type(value) != str:
            raise serializers.ValidationError("String Description Only")
        elif len(value) > 250:
            raise serializers.ValidationError("Description Is Too Long, Restrict To 250 Characters")
        else:
            return value