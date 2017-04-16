from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "landingpage/homepage.html");

def first_franchise(request):
    return render(request, "landingpage/franchise1.html");

def second_franchise(request):
    return render(request, "landingpage/franchise2.html");

def third_franchise(request):
    return render(request, "landingpage/franchise3.html");

def fourth_franchise(request):
    return render(request, "landingpage/franchise4.html");

def fifth_franchise(request):
    return render(request, "landingpage/franchise5.html");

def sixth_franchise(request):
    return render(request, "landingpage/franchise6.html");
