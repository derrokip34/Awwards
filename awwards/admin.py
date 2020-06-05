from django.contrib import admin
from .models import Profile,Category,Rating,Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Rating)