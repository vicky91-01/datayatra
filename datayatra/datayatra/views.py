from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate


def home(request):
  return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # form.save()
            login(request, user)
            return render(request, "home.html")  # redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
