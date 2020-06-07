from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Project
from datetime import timezone

# Create your tests here.
class ProjectTests(TestCase):
    def setUp(self):
        self.user = User(id=1,username='derrick',email='derrick@gmail.com',password='58744')
        self.user.save()
        self.project = Project(id=1,landing_page='ig.jpg',project_title='IG clone',project_description='Instagram clone',project_link='https://ig34.com/',user=self.user,posted_on='2020-06-07')
        self.project.save_project()

    def tearDown(self):
        Project.objects.all().delete()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.project,Project))

    def test_save_project_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_get_all_projects(self):
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_get_project_by_id(self):
        self.project.save_project()
        project = Project.get_project_by_id(1)
        self.assertEqual(project.id,1)

    def get_projects_by_user(self):
        self.project.save_project()
        projects = Project.get_project_by_user(1)
        self.assertTrue(len(projects)>0)
