from django import forms
from .models import Profile,Project
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','phone_number']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name',]

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','design_rating','content_rating','usability_rating']
        widgets = {
            'project_categories': forms.CheckboxSelectMultiple()
        }
