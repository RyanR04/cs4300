#Import deafult router and viewsets
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet,SeatViewSet,BookingViewSet,movie_list,book_seat, booking_history
from django.urls import path

#Set router to DefaultRouter to get MovieViewSet
router = DefaultRouter()

#Creater router url for movies,seats,and bookings apis 
router.register(r'movies',MovieViewSet)
router.register(r'seats',SeatViewSet)
router.register(r'bookings',BookingViewSet)

#Url routes for different parts of the website
urlpatterns = [
    #Path to get info for movie_list
    path('',movie_list,name = 'movie_list'),
    # Send Book/<The name of the movie based on ID>/ and call book_seat and seat for specific movie paths
    path('book/<int:movie_id>/',book_seat, name='book_seat'),
    #Now have history/booking history url 
    path('history/',booking_history,name = 'booking_history'),
    
] + router.urls
