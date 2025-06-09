from django.urls import path
from . import views

urlpatterns = [
    path('createmovie/',views.func)
]
