from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import FeedbackForm
import requests
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic import ListView

def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {settings.SPOTIFY_CLIENT_CREDENTIALS}"  # Base64 encode client_id:client_secret
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    return response_data.get('access_token', '')

def spotify_artist_search(request):
    query = request.GET.get('query', '')
    token = get_spotify_token()
    
    if not token:
        return JsonResponse({"error": "Spotify token not available"}, status=400)

    # Use Spotify's search API to search for artists
    search_url = f"https://api.spotify.com/v1/search?q={query}&type=artist"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(search_url, headers=headers)
    artists = response.json().get('artists', {}).get('items', [])
    results = [{"name": artist['name'], "id": artist['id']} for artist in artists]
    return JsonResponse({"artists": results})

@login_required
def feedback_view(request):
    context = {'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Associate the logged-in user with the feedback
            feedback.save()
            return redirect('thank_you')  # Replace with your success URL
    else:
        form = FeedbackForm()

    context['form'] = form

    return render(request, 'feedback.html', context=context)


def thank_you_view(request):
    return render(request, 'thank_you.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Feedback

@login_required
def profile_view(request):
    user_feedback = Feedback.objects.filter(user=request.user)
    paginator = Paginator(user_feedback, 5)  # Show 5 reviews per page
    page_number = request.GET.get('page')
    page_feedback = paginator.get_page(page_number)

    context = {
        'user': request.user,
        'feedback_list': page_feedback,
    }
    return render(request, 'profile.html', context)


class VenueFeedbackListView(ListView):
    model = Feedback
    template_name = 'venue_feedback_list.html'  # custom template
    context_object_name = 'feedback_list'  # name for the feedback list in the template
    paginate_by = 10

    def get_queryset(self):
        venue = self.kwargs.get('venue')
        return Feedback.objects.filter(venue__iexact=venue)


class ArtistFeedbackListView(ListView):
    model = Feedback
    template_name = 'artist_feedback_list.html'
    context_object_name = 'feedback_list'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        artist = self.kwargs.get('artist')
        return Feedback.objects.filter(artist__iexact=artist)



