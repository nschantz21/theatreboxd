from django.db import models

class Feedback(models.Model):
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    venue = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    venue_rating = models.CharField(max_length=1, choices=RATING_CHOICES)  # Dropdown field
    artist_rating = models.CharField(max_length=1, choices=RATING_CHOICES)  # Dropdown field

    comments = models.TextField()

    def __str__(self):
        return self.name
