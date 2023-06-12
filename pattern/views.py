from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def pattern(request):
    return render(request, "index.html")

