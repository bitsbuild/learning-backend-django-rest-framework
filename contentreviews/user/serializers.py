from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer,CharField
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True,style={'input_type':'password'})
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']
        extra_kwargs = {
            'password':{'write_only':True},
            'style':{'input_type':'password'},
        }