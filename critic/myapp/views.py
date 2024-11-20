from django.shortcuts import render, redirect
from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('thank_you')  # Redirect to a thank-you page
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def thank_you_view(request):
    return render(request, 'thank_you.html')

