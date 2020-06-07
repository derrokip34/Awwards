from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Project,Rating
from .forms import UpdateUserForm,UpdateProfileForm,PostProjectForm,RatingForm
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from django.http import Http404

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user

    projects = Project.get_all_projects()
    title = 'Welcome to Awwards'
    return render(request, 'index.html',{'title':title,'current_user':current_user,'projects':projects})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    current_user = request.user
    user = User.objects.filter(id=id).first()
    user_profile = user.profile
    projects = Project.get_project_by_user(id)

    title = f'{user.username} profile'
    return render(request,'profile/profile.html',{'title':title,'current_user':current_user,'user':user,'profile':user_profile,'projects':projects})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('userProfile',id=current_user.id)

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    title = f'Update {current_user.username} profile'
    return render(request,'profile/update_profile.html',{'title':title,'current_user':current_user,'u_form':user_form,'p_form':profile_form})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    current_user = request.user
    project = Project.objects.filter(id=project_id).first()
    ratings = Rating.objects.filter(project_id=project_id)
    usability_rating = Rating.objects.filter(project_id=project_id).aggregate(Avg('usability'))
    content_rating = Rating.objects.filter(project_id=project_id).aggregate(Avg('content'))
    design_rating = Rating.objects.filter(project_id=project_id).aggregate(Avg('design'))

    title = f'{project.project_title} details'
    return render(request,'project.html',{'title':title,'project':project,'current_user':current_user,'ratings':ratings,'usability_rating':usability_rating,'content_rating':content_rating,'design_rating':design_rating})

@login_required(login_url='/accounts/login/')
def comment_and_rate(request,project_id):
    current_user = request.user
    project = Project.objects.filter(id=project_id).first()
    if request.method == 'POST':
        rate_form = RatingForm(request.POST)
        if rate_form.is_valid():
            rating = rate_form.save(commit=False)
            rating.project = project
            rating.user = current_user
            rating.save()
            return redirect('project', project_id)
    else:
        rate_form = RatingForm()

    return render(request, 'rating.html',{'current_user':current_user,'rate_form':rate_form,'project':project})

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)

class ProfileDescription(APIView):
    def get_profile(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

class ProjectDescription(APIView):
    def get_project(self,pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)
