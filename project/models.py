from django.db import models
from django.urls import reverse

"""
Project
- title
- url (leading to the site)
- image 
- description (keep it short)
- category (foreignkey relationship to Category model)
- tags (many-to-many relationship to Tag model)

==================
Category
- name

==================
Tag
- name
"""


class Project(models.Model):
    class Meta:
        ordering = ["-id"]  # Always show latest projects first
        verbose_name_plural = "Projects"

    title = models.CharField(max_length=50)
    url = models.URLField()
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="categories")
    tags = models.ManyToManyField("Tag", verbose_name="tags")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("index")


class Category(models.Model):
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")


class Tag(models.Model):
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")
