from django.db import models
from django.urls import reverse

"""
Contact
    - first_name
    - last_name
    - email (Unique = True)
    - phone_number
    - is_subscribed
"""


class Contact(models.Model):
    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Contacts"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14)
    is_subscribed = models.BooleanField()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("index")
