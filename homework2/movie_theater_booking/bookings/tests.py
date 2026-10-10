from django.test import TestCase,Client
from .models import Movie,Seat,Booking
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


# Create your tests here.

#Unit Tests Check to see if we can make our models 

#Test to see if creating all Models can they be made

#Model Test Case
class MovieTestCase(TestCase):
    #Test to see if models works fine 
    def test_Movie_Creation(self):
        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)

        #Is the Movie Made
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(movie.description, "Sciecne Fiction")
        self.assertEqual(str(movie.release_date), "2010-07-16")
        self.assertEqual(movie.duration, 148)

#SeatTestCase
class SeatTestCase(TestCase):
    #Test to see if seat works fine
    def test_Seat_Creation(self):
        #Create a seat
        seat = Seat.objects.create(seat_number=1,booking_status=False)

        #Is the seat made
        self.assertEqual(seat.seat_number,1)
        self.assertEqual(seat.booking_status,False)

#BookingTestCase
class BookingTestCase(TestCase):

    #Test to see if bookings works fine
    def test_Booking_Creation(self):

        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
        #Create the seat
        seat = Seat.objects.create(seat_number=1,booking_status=False)
        #User object from the import of django
        user = User.objects.create_user(username='test_user')

        #Booking objcets linking to movie,seat,and user
        booking = Booking.objects.create(movie = movie,seat =seat,user=user)

        #Pass the foriegn keys to see if they have them
        self.assertEqual(movie,movie)
        self.assertEqual(seat,seat)
        self.assertEqual(user,user)



#Integration Test for API's

class MoviesAPITesting(TestCase):
    #Can we pull from Movie API
    def test_Movie_API_Implementation(self):

        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciencne Fiction",release_date="2010-07-16",duration=148)

        #THIS LINE BELOW REQUIRED ME TO USE AI TO UNDERSTAND HOW TO used client() and its basic commands to simulate a user in a test
        #This info is used throughout the program.
        response = self.client.get('/api/movies/')

        #Check to see if it returns a stATUS code of 200 meaning the path is reached
        self.assertEqual(response.status_code,200)
        #Check to see how much data in the api and whats in it.
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['title'],"Inception")
        self.assertEqual(response.data[0]['description'],"Sciencne Fiction")
        self.assertEqual(response.data[0]['release_date'],"2010-07-16")
        self.assertEqual(response.data[0]['duration'],148)



class SeatAPITesting(TestCase):
    #Call we pull from seats api 
    def test_Seat_API_Testing(self):
        #Create seat objects
        seat = Seat.objects.create(seat_number=1,booking_status=False)
        seat = Seat.objects.create(seat_number=2,booking_status=True)
        seat = Seat.objects.create(seat_number=3,booking_status=False)

        #Store the API info from response
        response = self.client.get('/api/seats/')

        #Check if we got 200 status code and see variouse points to check seat data
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data),3)
        self.assertEqual(response.data[0]['seat_number'],1)
        self.assertEqual(response.data[1]['booking_status'],True)


class BookingsAPITesting(TestCase):
    #Test to see if we have bookins stored
    def test_Bookings_API_Testing(self):
        
        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
        #Create the seat
        seat = Seat.objects.create(seat_number=1,booking_status=False)
        #User object from the import from django to create a test_user
        user = User.objects.create_user(username='test_user')

        #Making a booking object linked to these objects
        booking = Booking.objects.create(movie = movie,seat =seat,user=user)

        #Get the booking from the bookings API
        response = self.client.get('/api/bookings/')

        #Check to see if api was reached and if the booking match the other object info
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['movie'],movie.id)
        self.assertEqual(response.data[0]['seat'],seat.id)
        self.assertEqual(response.data[0]['user'],user.id)


# Used to test if booking behavior works 
class TestBookingBehavior(TestCase):
    def test_booking_creates_record(self):
        #First make a client object
        self.client = Client()
        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
        #Create the seat
        seat = Seat.objects.create(seat_number=1,booking_status=False)

        #User object from the import of django, to make an actually user object to test if we can book something
        user = User.objects.create_user(username='test_user',password='test_password')
        #Foce login so we have a user asscoiated with the booking record to simulate and actual user
        self.client.force_login(user)

        #Check what happens when we post/make a booking 
        response = self.client.post( f'/api/book/{movie.id}/',{'seat_id':seat.id})

        #Check to see if status code is 200 meaning it worked and see if a bookingobject now exists.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 1)