from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(default='anonymous.png',upload_to='profile_pics/')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(unique=True,blank=True)
    phone_number = models.CharField(max_length=10,blank=True)

class Category(models.Model):
    category = models.CharField(max_length=50)

class Project(models.Model):
    landing_page = models.ImageField(upload_to='landing_page')
    project_title = models.CharField(max_length=50)
    project_description = models.TextField()
    project_link = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    design_rating = models.IntegerField(default=0)
    content_rating = models.IntegerField(default=0)
    usability_rating = models.IntegerField(default=0)
    project_categories = models.ManyToManyField(Category)

class Rating(models.Model):
    CHOICES = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)

    design = models.IntegerField(choices=CHOICES,blank=True,default=0)
    usability = models.IntegerField(choices=CHOICES, blank=True,default=0)
    creativity = models.IntegerField(choices=CHOICES, blank=True,default=0)
    content = models.IntegerField(choices=CHOICES, blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
