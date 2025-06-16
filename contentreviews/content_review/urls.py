from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-apis/','app.urls'),
]
