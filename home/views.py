from django.shortcuts import render
from .models import Destination
#from tour.models import Tournament


def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})

