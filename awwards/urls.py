from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^profile/id/(?P<id>\d+)',views.profile,name='userProfile'),
    url(r'^update_profile/',views.update_profile,name='updateProfile'),
    url(r'^post_project/',views.post_project,name='newProject'),
    url(r'^project/(?P<project_id>\d+)',views.project,name='project'),
    url(r'^rate_&_comment/(\d+)',views.comment_and_rate,name='rate'),
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^api/project/$',views.ProjectList.as_view()),
    url(r'^api/profile/profile_id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url(r'^api/project/project_id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)