from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
def logout():
    return 1
def register():
    return 0
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',obtain_auth_token,name='login'),
    path('logout/',logout,name='logout'),
]
