# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'email', 'password', 'confirmpassword']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'email', 'password', 'confirmpassword']
        widgets = {
            'password':forms.PasswordInput(),
            'confirmpassword': forms.PasswordInput()

        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']
        widgets = {
            'bio':forms.Textarea(attrs={'class': 'form-control', 'row':3})
        }