from rest_framework.viewsets import ModelViewSet
from user.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST'])
def account_deletion(request):
    try:
        request.user.delete()
        return Response({'status':'Account Deleted Successfully'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'status':'Account Deletion Failed','error':str(e)},status=status.HTTP_400_BAD_REQUEST)
class UserRegistrationVS(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
