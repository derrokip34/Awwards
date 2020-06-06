from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Project,Category
from .forms import UpdateUserForm,UpdateProfileForm,PostProjectForm

# Create your views here.
def home(request):
    current_user = request.user

    title = 'Welcome to Awwards'
    return render(request, 'index.html',{'title':title,'current_user':current_user})

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

def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        project_form = PostProjectForm(request.POST,request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
    else:
        project_form = PostProjectForm()

    title = 'New Project'
    return render(request,'new_project.html',{'title':title,'project_form':project_form,'current_user':current_user})
