import email
from django import forms
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

# Models
from .models import Contact

"""
ContactForm(ModelForm)
    # Model Fields
    - first_name
    - last_name
    - email
    - phone_number
    - subscribed ( Boolfield to see if they want to recieve promotional data or not )

    # Extra fields
    - subject ( choicefield of what their requirements are )
    - message/description
    - files ( optional field to upload files if needed )

    Methods
    -- register email for promotional emails ( make this shorter pls. ) 
    -- send mail
"""


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=14)
    is_subscribed = forms.BooleanField(
        initial=False,
        required=False,
        label="Do you want to subscribe to our newsletter?",
    )
    message = forms.CharField(widget=forms.Textarea())
    subject = forms.CharField(max_length=255)
    files = forms.FileField(
        required=False,
        help_text="Add any relevant files here if you have a design/idea drawn up already.",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )

    def create_contact_model(self):
        form = self.clean()

        if not Contact.objects.filter(email=form["email"]).exists():
            Contact.objects.create(
                first_name=form["first_name"],
                last_name=form["last_name"],
                email=form["email"],
                phone_number=form["phone_number"],
                is_subscribed=form["is_subscribed"],
            )

    def send_email(self):
        form = self.clean()

        first_name = form["first_name"]
        last_name = form["last_name"]
        email = form["email"]
        phone_number = form["phone_number"]
        message = form["message"]
        subject = form["subject"]
        files = self.files.getlist("files")

        message = f"{first_name} {last_name}\n{email}\n{phone_number}\n\n{message}"

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=email,
            to=(settings.HOST_EMAIL,),
        )

        if files:
            for file in files:
                email.attach(file.name, content=file.content_type)

        email.send()
