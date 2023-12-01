from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "ratings/index.html"
    context_object_name = "latest_show_list"

    def get_queryset(self):
        """Return the last five published questions."""
        #return Shows.objects.order_by("-pub_date")[:5]
        pass