from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('spotify-artist-search/', views.spotify_artist_search, name='spotify_artist_search'),
    path('profile/', views.profile_view, name='profile'),
    path('feedback/venue/<str:venue>/', views.VenueFeedbackListView.as_view(), name='venue_feedback_list'),
    path('feedback/artist/<str:artist>/', views.ArtistFeedbackListView.as_view(), name='artist_feedback_list'),
    path('', views.profile_view, name='home')
]
