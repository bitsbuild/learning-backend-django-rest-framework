from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user.views import UserRegistrationAV
def logout():
    return 1
urlpatterns = [
    path('register/',UserRegistrationAV,name='register'),
    path('login/',obtain_auth_token,name='login'),
    path('logout/',logout,name='logout'),
]
