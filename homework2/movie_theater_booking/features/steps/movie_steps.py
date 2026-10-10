from behave import given,when,then 
from django.test import Client
from bookings.models import Movie

@given('a movie exists')
def step_movie_exists(context):
    #Create a movie
    context.Movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)

@when ('the user opens the movie listings page')
def get_Movie_From_API(context):
    #See if we can get it from page
    context.response = Client().get('/api/')

@then ('the movie title should appear')
def see_Movie_Title(context):
    #If so then we should a status of 200 and Inception as part of the content
    assert context.response.status_code == 200
    assert b'Inception' in context.response.content