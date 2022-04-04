from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def AboutUs(request):
    return render(request, 'aboutus.html', {'title': 'About Us'})

def ContactUs(request):
    return render(request, 'contactus.html', {'title': 'Contact Us'})

def Products(request):
    return render(request, 'products.html', {'title': 'Products'})
