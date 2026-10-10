#BELOW I USED AI TO HELP SETUP BEHAVIOR TESTS
#Lets us use the env vars
import os
#Used to help initilize frame work
import django

#Setup for env vars
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "movie_theater_booking.settings")

#Initializes it for django
django.setup()