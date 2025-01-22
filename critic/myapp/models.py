from django.db import models
from django.contrib.auth.models import User
import datetime
import django.utils.timezone

class Venue(models.Model):
    name = models.CharField(max_length=255)
    place_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    spotify_artist_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate with User
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    venue_rating = models.CharField(max_length=1, choices=RATING_CHOICES)  # Dropdown field
    artist_rating = models.CharField(max_length=1, choices=RATING_CHOICES)  # Dropdown field
    date_of_performance = models.DateField(default=django.utils.timezone.now)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}-{self.venue.name}-{self.artist.name if self.artist else 'No Artist'}"
