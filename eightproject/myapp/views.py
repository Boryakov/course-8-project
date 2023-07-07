from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def view(request):
    return HttpResponse('Okay')