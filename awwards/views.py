from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Project,Category
from .forms import UpdateUserForm,UpdateProfileForm

# Create your views here.
def home(request):
    current_user = request.user

    title = 'Welcome to Awwards'
    return render(request, 'index.html',{'title':title})

def profile(request,id):
    current_user = request.user
    user = User.objects.filter(id=id).first()
    user_profile = user.profile

    title = f'{user.username} profile'
    return render(request,'profile/profile.html',{'title':title,'current_user':current_user,'user':user,'profile':user_profile})

def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile',id=current_user.id)

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    title = f'Update {current_user.username} profile'
    return render(request,'profile/update_profile.html',{'title':title,'current_user':current_user,'u_form':user_form,'p_form':profile_form})
