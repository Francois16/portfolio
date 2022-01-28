from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

# Models
from .models import Project, Category, Tag


class ProjectTests(TestCase):
    def setUp(self):

        self.project = Project.objects.create(
            title="Oaks on Main Shopping Center",
            url="www.oaksonmain.co.za",
            image=SimpleUploadedFile(
                name="test.jpg",
                content=b"a",
                content_type="image/jpeg",
            ),
            description="Beautiful website created for Oaks on Main Shopping Center in Knysna!",
            category=Category.objects.create(name="Website"),
        )

        self.tag = Tag.objects.create(name="HTML5")
        self.project.tags.add(self.tag)

    def test_project_model(self):
        self.assertEqual(f"{self.project.title}", "Oaks on Main Shopping Center")
        self.assertEqual(f"{self.project.url}", "www.oaksonmain.co.za")
        self.assertEqual(
            f"{self.project.description}",
            "Beautiful website created for Oaks on Main Shopping Center in Knysna!",
        )
        self.assertEqual(self.project.tags.count(), 1)
        self.assertEqual(self.project.category.name, "Website")
        self.assertTrue(self.project.image.url.endswith(".jpg"))

    def test_project_listview(self):
        resp = self.client.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.project.title)
        self.assertTemplateUsed(resp, "page/index.html")
