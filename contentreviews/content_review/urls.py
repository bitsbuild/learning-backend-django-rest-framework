from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-apis/',include('app.urls')),
    path('user/',include('user.urls')),
]
