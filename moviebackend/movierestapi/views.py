from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
def sample_function(request):
    return HttpResponse("Sample Function Working Very Well")