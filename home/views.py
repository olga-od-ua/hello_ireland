""" A Module to create the Home Page views """
from django.shortcuts import render


# Create your views here.
def index(request):
    """ A view to rended the Home Page """

    return render(request, "home/index.html")
