from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^profile/id/(?P<id>\d+)',views.profile,name='profile'),
    url(r'^update_profile/',views.update_profile,name='updateProfile'),
]