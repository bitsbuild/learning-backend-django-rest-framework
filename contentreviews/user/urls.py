from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from user.views import create_account 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('create/',create_account,name='create'),
    # path('token/',obtain_auth_token,name='token'),
    # path('delete/',delete_account,name='delete')
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]