from rest_framework import viewsets
from django.shortcuts import render
from .models import Movie,Booking,Seat
from .serializers import MovieSerializer,BookingSerializer,SeatSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    #Get all instance of movie
    queryset = Movie.objects.all()
    #Get Serializer for JSON formating
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    #Get all seat instances
    queryset = Seat.objects.all()
    #Get Serializer for JSON formating
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    #Get all instance of bookings
    queryset = Booking.objects.all()
    #Get Serializer for JSON formating
    serializer_class = BookingSerializer