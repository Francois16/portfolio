from django.forms import ValidationError
from django.shortcuts import redirect

from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.create_contact_model()
            form.send_email()
        else:
            raise ValidationError(f"Form was not valid with errors: {form.errors.as_data()}")

    return redirect("index")
