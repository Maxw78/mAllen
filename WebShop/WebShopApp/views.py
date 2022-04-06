from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {'u_form': u_form, 'p_form': p_form}
        return render(request, 'profile.html', context)