from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from user.serializers import UserSerializer
from django.contrib.auth.models import User
class UserRegistrationAV(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
