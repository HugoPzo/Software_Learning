from django.contrib import admin
from .models import SkillTag, Project

# Skill tag to admin
admin.site.register(SkillTag)

# Projects to admin
admin.site.register(Project)