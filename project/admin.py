from django.contrib import admin

# Models
from .models import Project, Category, Tag

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Tag)
