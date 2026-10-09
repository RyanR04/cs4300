#For Bleow Code had to as AI to figure out how to do so
import os
import django


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "movie_theater_booking.settings")

django.setup()