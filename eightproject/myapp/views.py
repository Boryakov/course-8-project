from django.shortcuts import render
from rest_framework import generics, viewsets

from . import serializers, models



def view(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):

    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):

    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer