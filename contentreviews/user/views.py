from rest_framework.viewsets import ModelViewSet
from user.serializers import UserSerializer
from django.contrib.auth.models import User
class UserRegistrationVS(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer