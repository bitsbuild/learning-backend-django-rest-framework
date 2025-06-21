from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user.views import UserRegistrationVS,logout
urlpatterns = [
    path('register/',UserRegistrationVS.as_view({'post':'create'},name='register')),
    path('login/',obtain_auth_token,name='login'),
    path('logout/',logout,name='logout'),
]
