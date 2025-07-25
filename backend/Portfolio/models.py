from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.CharField(max_length=255, blank=True)
    tech_stack = models.CharField(max_length=255, blank=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
