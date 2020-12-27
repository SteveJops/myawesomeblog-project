from django.shortcuts import render
from django.views import View
from .models import EventModel


class HomeView(View):
    def get(self, request):
        events = EventModel.objects
        return render(request, 'events/home.html', {'events': events})

# Create your views here.
