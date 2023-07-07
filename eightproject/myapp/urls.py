from django.urls import path
from .views import view

urlpatterns = [
    path('check', view), 
]