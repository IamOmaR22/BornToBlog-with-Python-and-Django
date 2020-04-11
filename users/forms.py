from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Required is True in default. So i keep it default

    class Meta:
        model = User # Whenever the form is validate it is going to create a new user
        fields = ['username', 'email', 'password1', 'password2']