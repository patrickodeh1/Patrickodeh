from django.db import models


class Tech(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='tech_icons/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.CharField(max_length=255, blank=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')
    techs = models.ManyToManyField(Tech, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
