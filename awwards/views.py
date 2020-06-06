from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile,Project,Category

# Create your views here.
def home(request):

    title = 'Welcome to Awwards'
    return render(request, 'index.html',{'title':title})

def profile(request,id):
    current_user = request.user
    user = User.objects.filter(id=id).first()
    user_profile = user.profile

    title = f'{user.username} profile'
    return render(request,'profile/profile.html',{'title':title,'current_user':current_user,'user':user,'profile':user_profile})
