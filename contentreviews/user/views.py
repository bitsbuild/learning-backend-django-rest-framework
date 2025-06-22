from user.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
@api_view(['POST'])
def create_account(request):
    username = request.data['username']
    password = request.data['password']
    confirm_password = request.data['confirm_password']
    email = request.data['email']
    if confirm_password == password:
        user = {
            "username":username,
            "password":password,
            "email":email
        }
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            user_token_search = User.objects.get(username=username)
            token,collect = Token.objects.get_or_create(user=user_token_search)
            return Response({
                "status":"Account Created Successfully",
                "token":str(token.key)
            },status=status.HTTP_200_OK)
        else:
            return Response({
                "status":"Account Creation Failed",
                "error":str(serializer.errors)
            },status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            "status":"Account Creation Failed",
            "error":str(serializer.errors)
        },status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def delete_account(request):
    try:    
        request.user.delete()
        return Response({
            "status":"Account Deletion Successful"
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "status":"Account Deletion Failed",
            "error":str(e)
        },status=status.HTTP_400_BAD_REQUEST)