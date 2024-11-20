from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name', 'email', 'comments', 'artist',
            'venue_rating', 'artist_rating'
        ]
        widgets = {
            'venue': forms.TextInput(attrs={'id': 'venue-input'}),
        }
