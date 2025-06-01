from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    Render the index page of the practice app.
    """
    return HttpResponse("<h1>Welcome to Data-Yatra Project: Practice App</h1>")
