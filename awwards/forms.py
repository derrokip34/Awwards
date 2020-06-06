from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','phone_number']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name',]
