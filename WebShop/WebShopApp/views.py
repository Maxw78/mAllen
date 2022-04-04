from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Welcome to the WebShop')

def AboutUs(request):
    return HttpResponse('About Us')

def ContactUs(request):
    return HttpResponse('ContactUs')

def Products(request):
    return HttpResponse('Product')
