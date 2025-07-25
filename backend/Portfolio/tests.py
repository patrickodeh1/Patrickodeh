from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Tech
from django.core.files.uploadedfile import SimpleUploadedFile

class PortfolioTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Create Tech instances
        python = Tech.objects.create(name='Python')
        django = Tech.objects.create(name='Django')

        # Create image file mock
        image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")

        # Create project
        test_project = Project.objects.create(
            name='Test Project',
            description='This is a test project.',
            short_description='Short desc',
            github_link='https://github.com/',
            live_link='https://example.com/',
            image=image
        )

        # Add tech stacks to project
        test_project.techs.add(python, django)

    def test_project_creation(self):
        project = Project.objects.get(name='Test Project')
        self.assertEqual(project.description, 'This is a test project.')
        self.assertTrue(project.techs.filter(name='Python').exists())
        self.assertTrue(project.techs.filter(name='Django').exists())
        
