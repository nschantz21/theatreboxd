from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    artist = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'id': 'id_artist', 'placeholder': 'Search for an artist...'})
    )
    venue = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'id': 'venue-input', 'placeholder': 'Search for a venue...'})
    )

    class Meta:
        model = Feedback
        fields = [
            'artist', 'artist_rating', 'venue',
            'venue_rating', 'date_of_performance',
            'comments', 
        ]
