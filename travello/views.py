from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):
    # Destination 1
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})