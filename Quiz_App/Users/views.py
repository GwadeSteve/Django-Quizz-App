from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required

def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(name=form.cleaned_data['name'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Registration. Try again!")
    else:
        form = CustomUserCreationForm()
    return render(request, 'Users/register.html', {'form': form})

def Login(request):
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(request, name=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials. Please check name and password.')
    else:
        form = CustomUserLoginForm()
    return render(request, 'Users/login.html', {'form': form})

@login_required
def Logout(request):
    logout(request)
    return redirect('/')
