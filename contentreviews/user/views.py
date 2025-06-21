from django.shortcuts import render
from rest_framework.generics import CreateAPIView
class UserRegistrationAV(CreateAPIView):
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)