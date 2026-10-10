from rest_framework import viewsets
from django.shortcuts import render
from .models import Movie,Booking,Seat
from .serializers import MovieSerializer,BookingSerializer,SeatSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    #Get all instance of movie
    queryset = Movie.objects.all()
    #Get Serializer for JSON formating
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    #Get all seat instances
    queryset = Seat.objects.all().order_by('seat.number')
    #Get Serializer for JSON formating
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    #Get all instance of bookings
    queryset = Booking.objects.all()
    #Get Serializer for JSON formating
    serializer_class = BookingSerializer

#If not login via admin panel not acccess to Booking A Seat (Simulates having an account)
@login_required
#Used for Book Seat to get the id for the specifc movie and all seat objects with it
def book_seat(request,movie_id):
    #Get ID of instance of movie to find the specific one
    movie = Movie.objects.get(id = movie_id)
    #Get all seats from database 
    seats = Seat.objects.all()

    #Needed AI Assistance to brainstorm and implement the Section Below
    #Create a list to store all bookings first filter by looking at what movies match what booking, then from that
    #specific value i only need the seat_id. (AI HELP PART)Flat true will just make it a single value and not a tuple
    #This regenerate for each movie. The list makes it so all bookings on all accounts are independent. As the lists are unique to them.
    bookings_list = Booking.objects.filter(movie = movie).values_list('seat_id',flat=True)
    my_bookedseats = Booking.objects.filter(movie = movie,user = request.user).values_list('seat_id',flat=True)

    #Check to see if button is clicked the we get POST
    if request.method == "POST":
        #Get seatdata from the input line in HTML
        seat_id = request.POST.get('seat_id')
        #Go get specific seat object we need
        seat = Seat.objects.get(id=seat_id)

        #First check if the booking object exists or is booked, if so then clicking it again cancels it
        if Booking.objects.filter(movie=movie, seat=seat, user = request.user).exists():

            #Get that specifc booking object make sure to check if this user has it 
            booking = Booking.objects.get(movie = movie, seat = seat, user = request.user)
            
            # If so Delete it
            booking.delete()

            #The Bookings Open
            seat.booking_status=False

        #If another user has this then doing nothing
        elif Booking.objects.filter(movie=movie, seat=seat).exists():
            pass
        #If no one has it book it
        else:
            #Create a new booking object
            Booking.objects.create(movie = movie, seat = seat,user= request.user)
            
            #Chnage the booking status
            seat.booking_status=True

        #Update seat withnew status
        seat.save()

    #Sends to html file
    return render(request,'bookings/seat_booking.html',{'movie':movie,'seats':seats,'bookings_list':bookings_list,'my_bookedseats':my_bookedseats})



#This returns the list to the html of all movies and the data it has
def movie_list(request):
    #Get all Movie Obejcts
    movies = Movie.objects.all()
    #Return for html movie_list to display
    return render(request, 'bookings/movie_list.html', {'movies': movies})

#If not login via admin panel not acccess to Booking History (Simulates having an account)
@login_required
#For booking histroy it sends all data for html
def booking_history(request):
    #Filter bookings by user
    bookings = Booking.objects.filter(user=request.user)
    #Return the info to display
    return render(request,'bookings/booking_history.html',{'bookings':bookings})