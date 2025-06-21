from rest_framework.viewsets import ModelViewSet
from user.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST'])
def logout(request):
    try:
        request.user.auth_token.delete()
        return Response({'status':'Logged Out Successfully'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'status':'Log Out Failed','error':str(e)},status=status.HTTP_400_BAD_REQUEST)
class UserRegistrationVS(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
