# The Testing File Name Should Not Be Changed
# The Endpoints Testing Function Should Begin With "test_x" Strictly As Thier Function Name
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class UserTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="jashupadhyay",password="12345678")
    def test_create_user_success(self):
        data = {
            "username":"testcase",
            "password":"jash_password",
            "confirm_password":"jash_password",
            "email":"testcase@example.come"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_gettoken_user_success(self):
        data = {
            "username":"jashupadhyay",
            "password":"12345678"
        }
        response = self.client.post(reverse('token'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_delete_user(self):
        self.token = Token.objects.get(user__username='jashupadhyay')
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        respone = self.client.post(reverse('delete'))
        self.assertEqual(respone.status_code,status.HTTP_200_OK)