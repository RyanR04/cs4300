#Import deafult router and viewsets
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet,SeatViewSet,BookingViewSet

#Set router to DefaultRouter to get MovieViewSet
router = DefaultRouter()

#Creater router url for movies,seats,and bookings
router.register(r'movies',MovieViewSet)
router.register(r'seats',SeatViewSet)
router.register(r'bookings',BookingViewSet)

urlpatterns = router.urls