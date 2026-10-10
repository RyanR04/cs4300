from behave import given,when,then 
from django.test import Client
from bookings.models import Seat,Movie
from django.contrib.auth.models import User

@given('a movie seat exists')
def step_MovieandSeat_exists(context):
    #Make Movie and seat
    context.movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
    context.seat = Seat.objects.create(seat_number=1,booking_status=False)

    #THIS PART BELOW WAS MADE WITH AI, AS I HAD TO FIGURE OUT HOW TO CREATE AND SIMUALTE A USER

    #First make context context.user and created stores a bool True or False if a new one is made get_or_create checks 
    #to see if the user was made or needs to be
    context.user, created = User.objects.get_or_create(username="user1")
    
    #If a new user needs to be made for the test
    if created:
        #Set a passtword 
        context.user.set_password("test_password")
        #Save the user
        context.user.save()

    #Now we make a client and login with user so it can be used for bookings
    context.client = Client()
    context.client.force_login(context.user)

    #No more AI use below this line


@when ('the user opens the booking page')
def get_Seat_From_API(context):
    #Check to see if we can see bookings based on movie
    context.response = context.client.get(f'/api/book/{context.movie.id}/')

@then ('all seats should appear')
def see_what_Seats_are_available(context):
    #If soo we get status 200
    assert context.response.status_code == 200
    #Check to see if seat 1 is shown in content
    assert b'1' in context.response.content