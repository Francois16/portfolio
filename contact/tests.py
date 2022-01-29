from django.test import TestCase
from django.urls import reverse

# Forms
from .models import Contact


class ContactForm(TestCase):
    def setUp(self):

        self.data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@email.com",
            "phone_number": "0766387260",
            "subject": "A subject",
            "message": "My message to you!",
            # "files": None,
            "subscribed": True,
        }

        self.resp = self.client.post("/contact/", data=self.data)
        self.html_resp = self.client.get("/")

    def test_contact_redirect(self):
        self.assertRedirects(self.resp, "/")

    def test_contact_model_was_created(self):
        self.assertEqual(Contact.objects.count(), 1)

    def test_contact_with_same_email_is_not_created_twice(self):
        self.client.post("/contact/", data=self.data)
        self.client.post("/contact/", data=self.data)
        self.assertEqual(Contact.objects.count(), 1)

    def test_form_fields_are_rendering(self):
        self.assertContains(self.html_resp, "first_name")
        self.assertContains(self.html_resp, "files")

    def test_status_code(self):
        self.assertEqual(self.resp.status_code, 302)


class TestContactModel(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            first_name="John",
            last_name="Doe",
            email="test@email.com",
            phone_number="123456789",
            is_subscribed=False,
        )

    def test_model_str(self):
        self.assertEqual(str(self.contact), self.contact.email)

    def test_get_absolute_url(self):
        self.assertEqual(self.contact.get_absolute_url(), "/")
