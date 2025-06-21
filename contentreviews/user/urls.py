from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from user.views import UserRegistrationVS
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'register',UserRegistrationVS,basename='register')
def logout():
    return 1
urlpatterns = [
    path('',include(router.urls)),
    path('login/',obtain_auth_token,name='login'),
    path('logout/',logout,name='logout'),
]
