from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(default='anonymous.png',upload_to='profile_pics/')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Project(models.Model):
    landing_page = models.ImageField(upload_to='landing_page')
    project_title = models.CharField(max_length=50)
    project_description = models.TextField()
    project_link = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title

    def save_project(self):
        self.save()

    @classmethod
    def get_all_projects(cls):
        projects = Project.objects.all()
        return projects

    @classmethod
    def get_project_by_id(cls,id):
        project = Project.objects.filter(id=id).first()
        return project

class Rating(models.Model):
    CHOICES = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)

    design = models.IntegerField(choices=CHOICES,blank=True,default=0)
    usability = models.IntegerField(choices=CHOICES, blank=True,default=0)
    content = models.IntegerField(choices=CHOICES, blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'{self.project.project_title} ratings'
