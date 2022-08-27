from dataclasses import fields
from email.mime import image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UpdateProfileForm(forms.ModelForm):
    image=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    phoneno=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control-file'}))

    class Meta:
        model=Profile
        fields=['image','phoneno']