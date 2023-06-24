from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def creativecenter(request):
    return render(request, "center.html")

