from django.urls import path
from movierestapi.views import sample_function
urlpatterns = [
    path('sample/',sample_function),
]
