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

    def test_Seat_Creation(self):
        seat = Seat.objects.create(seat_number=1,booking_status=False)
    
        self.assertEqual(seat.seat_number,1)
        self.assertEqual(seat.booking_status,False)

#BookingTestCase
class BookingTestCase(TestCase):

    def test_Booking_Creation(self):

        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
        #Create the seat
        seat = Seat.objects.create(seat_number=1,booking_status=False)
        #User object from the import of django
        user = User.objects.create_user(username='test_user')

        booking = Booking.objects.create(movie = movie,seat =seat,user=user)

        #Pass the foriegn keys to see if they have them
        self.assertEqual(movie,movie)
        self.assertEqual(seat,seat)
        self.assertEqual(user,user)



#Integration Test for API's

class MoviesAPITesting(TestCase):

    def test_Movie_API_Implementation(self):

        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciencne Fiction",release_date="2010-07-16",duration=148)

        #Needed AI assistance to understand how to get these folliwng lines below to find status code, and udnerstand how to test API
        response = self.client.get('/api/movies/')

        #Check to see if it returns a stsu code of 200 meaning the path is reached
        self.assertEqual(response.status_code,200)
        #Check to see how much data in the api
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['title'],"Inception")
        self.assertEqual(response.data[0]['description'],"Sciencne Fiction")
        self.assertEqual(response.data[0]['release_date'],"2010-07-16")
        self.assertEqual(response.data[0]['duration'],148)



class SeatAPITesting(TestCase):

    def test_Seat_API_Testing(self):
        seat = Seat.objects.create(seat_number=1,booking_status=False)
        seat = Seat.objects.create(seat_number=2,booking_status=True)
        seat = Seat.objects.create(seat_number=3,booking_status=False)

        response = self.client.get('/api/seats/')

        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data),3)
        self.assertEqual(response.data[0]['seat_number'],1)
        self.assertEqual(response.data[1]['booking_status'],True)


class BookingsAPITesting(TestCase):

    def test_Bookings_API_Testing(self):
        
        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
        #Create the seat
        seat = Seat.objects.create(seat_number=1,booking_status=False)
        #User object from the import of django
        user = User.objects.create_user(username='test_user')

        booking = Booking.objects.create(movie = movie,seat =seat,user=user)

        response = self.client.get('/api/bookings/')

        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['movie'],movie.id)
        self.assertEqual(response.data[0]['seat'],seat.id)
        self.assertEqual(response.data[0]['user'],user.id)


class TestBookingBehavior(TestCase):
    def test_booking_creates_record(self):
        self.client = Client()
        #Create a Movie
        movie = Movie.objects.create(title="Inception",description="Sciecne Fiction",release_date="2010-07-16",duration=148)
        #Create the seat
        seat = Seat.objects.create(seat_number=1,booking_status=False)

        #User object from the import of django
        user = User.objects.create_user(username='test_user',password='test_password')
        self.client.force_login(user)

        response = self.client.post( f'/api/book/{movie.id}/',{'seat_id':seat.id})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 1)