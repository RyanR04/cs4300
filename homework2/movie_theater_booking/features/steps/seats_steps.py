from behave import given,when,then 
from django.test import Client
from bookings.models import Seat,Movie
from django.contrib.auth.models import User

@given('a movie seat exists')
def step_MovieandSeat_exists(context):
    context.movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
    context.seat = Seat.objects.create(seat_number=1,booking_status=False)

    #This part below was amde with AI, as I had trouble figuring out how to create a user

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


@when ('the user opens the booking page')
def get_Seat_From_API(context):
    context.response = context.client.get(f'/api/book/{context.movie.id}/')

@then ('all seats should appear')
def see_what_Seats_are_available(context):
    assert context.response.status_code == 200
    assert b'1' in context.response.content