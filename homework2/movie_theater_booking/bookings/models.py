from django.db import models
from django.conf import settings

# Create your models here.

# Movie: title, description, release date, duration.
class Movie(models.Model):
    #All needed attributes for our Movie Model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()

#Seat: seat number, booking status.
class Seat(models.Model):

    #All needed attributes for Seat Model
    seat_number = models.PositiveIntegerField()
    booking_status = models.BooleanField(default=False)

#Booking: movie, seat, user, booking date.
class Booking(models.Model):

    # All needed attributes for Booking Model using foreign keys to relate to clases
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #Gets the booking time right when instance is created
    booking_date = models.DateTimeField(auto_now_add=True)

