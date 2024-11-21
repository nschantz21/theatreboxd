from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import FeedbackForm
import requests
from django.http import JsonResponse

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
            form.save()  # Save the form data to the database
            return redirect('thank_you')  # Redirect to a thank-you page
    else:
        form = FeedbackForm()
    context['form'] = form
    return render(request, 'feedback.html', context)


def thank_you_view(request):
    return render(request, 'thank_you.html')

