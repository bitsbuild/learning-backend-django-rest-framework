from rest_framework import serializers
from movierestapi.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    len_names = serializers.SerializerMethodField(

    )
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_len_names(self,object):
        return len(object.name)