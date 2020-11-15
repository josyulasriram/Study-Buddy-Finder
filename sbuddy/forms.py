from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'name', 'meetingURL', 'strengths', 'weaknesses', 'availability','phone_number']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'name', 'meetingURL', 'strengths', 'weaknesses', 'availability','phone_number']
