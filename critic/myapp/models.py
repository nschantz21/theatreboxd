from django.db import models
from django.contrib.auth.models import User
import datetime
import django.utils.timezone

class Feedback(models.Model):
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate with User
    venue = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=True, null=True)  # Optional artist field
    venue_rating = models.CharField(max_length=1, choices=RATING_CHOICES)  # Dropdown field
    artist_rating = models.CharField(max_length=1, choices=RATING_CHOICES)  # Dropdown field
    place_id = models.CharField(max_length=100, blank=True, null=True)
    place_address = models.TextField(blank=True, null=True)
    date_of_performance = models.DateField(default=django.utils.timezone.now)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}-{self.venue}-{self.artist}"
