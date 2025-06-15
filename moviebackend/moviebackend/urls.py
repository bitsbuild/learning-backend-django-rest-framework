from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title='Movies Application Backend',
        default_version = 'v1',
        description = 'Multiple Features Placeholder As Of Now',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie-rest-apis/',include('movierestapi.urls')),
    path('',schema_view.with_ui('swagger'),name='schema-swagger-ui'),
]
