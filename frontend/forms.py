from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from api.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
