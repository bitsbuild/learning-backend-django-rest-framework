from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
    def save(self):
        user = User(username=self.validated_data['username'],email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()