from django.db import models
import json

# Skill tags
class SkillTag(models.Model):
    skill_name = models.CharField(max_length=30)
    skill_image = models.ImageField(upload_to='images/', default='images/code.png')


    def __str__(self):
        return self.skill_name


class Project(models.Model):
    name = models.CharField(max_length=250, blank=True)
    myRole = models.CharField(max_length=250, null=True, blank=True)
    tools = models.JSONField(default=list, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default="No description")
    link = models.CharField(max_length=500, null=True, blank=True, default="#")

    def __str__(self):
        return self.name