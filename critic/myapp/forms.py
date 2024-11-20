from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name', 'email', 'comments', 
            'venue', 'artist',
            'venue_rating', 'artist_rating'
        ]
