from django.contrib.auth import login, logout, authenticate
from .forms import UserLoginForm, CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User


def user_register(request):
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user_auth = authenticate(email=email, password=raw_password)
            login(request, user_auth)
            messages.add_message(request, messages.INFO, 'User created!')
        else:
            messages.add_message(request, messages.ERROR, 'Uncorrect data. Try again!')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
