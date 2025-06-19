from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Content Review Backend',
        default_version='v1',
        description='Review Any Piece Of Content With The Help Of Wide Range Of Our APIs'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-apis/',include('app.urls')),
    path('',schema_view.with_ui('swagger'),name='schema-swagger-ui'),
]
