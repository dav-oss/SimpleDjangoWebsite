from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def geolocation(request):
    return render(request, 'geolocation.html')

def suites(request):
    return render(request, 'suites.html')

def contact(request):
    return render(request, 'contact.html')