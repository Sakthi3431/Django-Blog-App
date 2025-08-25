# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'email', 'password', 'confirmpassword']