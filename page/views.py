from django.shortcuts import render

# Models
from project.models import Project


def indexview(request):
    template_name = "page/index.html"

    projects = Project.objects.all()

    context = {
        "projects": projects,
    }

    return render(request, template_name, context)
