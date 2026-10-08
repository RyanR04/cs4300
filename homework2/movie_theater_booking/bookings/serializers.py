#Import all needed framework
from rest_framework import serializers
from .models import Movie,Seat,Booking

#MovieSerilizer
class MovieSerializer(serializers.ModelSerializer):
    #What meta data to use
    class Meta:
        model = Movie
        fields = '__all__' # Serializes all fields in the model 

# SeatSerializer
class SeatSerializer(serializers.ModelSerializer):
     class Meta:
        model = Seat
        fields = '__all__'


#BookingSerializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
