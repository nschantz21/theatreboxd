from django.shortcuts import render, redirect
from django.conf import settings
from .forms import FeedbackForm


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

