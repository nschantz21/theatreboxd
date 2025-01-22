from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    artist_name = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'id': 'artist-name', 'placeholder': 'Search for an artist...'})
    )
    venue_name = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'id': 'venue-name', 'placeholder': 'Search for a venue...'})
    )

    class Meta:
        model = Feedback
        fields = [
            'artist_name',
            'artist_rating', 
            'venue_name',
            'venue_rating', 'date_of_performance',
            'comments', 
        ]
