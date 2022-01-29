from django.shortcuts import render

# Models
from project.models import Project

# Forms
from contact.forms import ContactForm


def indexview(request):
    template_name = "page/index.html"

    projects = Project.objects.all()

    context = {
        "projects": projects,
        "contact_form": ContactForm,
    }

    return render(request, template_name, context)
