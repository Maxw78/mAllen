from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def AboutUs(request):
    return render(request, 'aboutus.html', {'title': 'About Us'})

def ContactUs(request):
    return render(request, 'contactus.html', {'title': 'Contact Us'})

def Products(request):
    return render(request, 'products.html', {'title': 'Products'})

def register(request):

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            form = UserRegisterForm()
            messages.success(request, f'Account not created yet')
        return render(request, 'register.html', {'form':form})
        
@login_required
def profile(request):
    return render(request, 'profile.html')