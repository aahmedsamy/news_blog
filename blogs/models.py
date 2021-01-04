from datetime import datetime

from django.db import models

# Create your models here.
from django.urls import reverse


class Author(models.Model):
    image = models.ImageField(upload_to="authors")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name', 'last_name']


class Category(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blogs:category-detail", self.id)

    class Meta:
        ordering = ['name']


def blog_image_path(instance, filename):
    _now = datetime.now()
    year = _now.year
    month = _now.month
    day = _now.day
    file_path = f"blogs/images/{instance.category}/{year}/{month}/{day}/{filename}"
    print(file_path)
    return file_path


class Blog(models.Model):
    image = models.ImageField(upload_to=blog_image_path)
    title = models.CharField("Title", max_length=256)
    body = models.TextField(max_length=2 ** 10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.category}: {self.title}"


