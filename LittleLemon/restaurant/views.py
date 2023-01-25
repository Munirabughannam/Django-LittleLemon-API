from django.shortcuts import render
from rest_framework import generics
from .serializers import BookingSerializer, MenuItemSerializer
from .models import MenuItems, Booking
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, 'index.html', {})


class MenuView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['Price']
    search_fields = ['Title']


class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer