from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
class UserTests(APITestCase):
    # The Testing File Name Should Not Be Changed
    # The Endpoints Testing Function Should Begin With "test_x" Strictly As Thier Function Name
    def test_create_user_success(self):
        data = {
            "username":"testcase",
            "password":"jash_password",
            "confirm_password":"jash_password",
            "email":"testcase@example.come"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_delete_user(self):
        pass