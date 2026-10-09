from behave import given,when,then 
from django.test import Client
from bookings.models import Seat,Movie,Booking
from django.contrib.auth.models import User

@given('a booking was made')
def step_MovieandSeatBooking_exists(context):
    #Create a Movie and Seat
    context.movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
    context.seat = Seat.objects.create(seat_number=1,booking_status=False)

    #This part below was made with AI, as I had trouble figuring out how to create a user

    #First make context contest.user and creted reutns a bool True or False if a new one is made get_or_create checks to see if the user was made or needs to be
    context.user, created = User.objects.get_or_create(username="user1")
    
    #If a new user needs to be amde for the test
    if created:
        #Set a passtword 
        context.user.set_password("test_password")
        #Save the user
        context.user.save()

    #Now we make a client and login with user so it can be used for bookings
    context.client = Client()
    context.client.force_login(context.user)

    #Create A Booking
    context.booking = Booking.objects.create(movie=context.movie,seat=context.seat,user=context.user)

@when ('the user opens the booking history page')
def get_Booking_API(context):
    context.response = context.client.get(f'/api/history/')

@then ('the booking will appear')
def see_what_Bookings_are_Booked(context):
    assert context.response.status_code == 200
    #Check to see if movie title is there
    assert b'Inception' in context.response.content
