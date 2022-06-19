from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=128,
                             label='email',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=128,
                                label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(max_length=128,
                                label='Password repeat',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=128,
                                label='email',
                                widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=128,
                               label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
