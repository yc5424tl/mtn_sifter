from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def json(self):
        return {'name': self.name}


class Source(models.Model):
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=3)
    language = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name="sources")
    url = models.URLField(blank=True, default="", max_length=150)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    @property
    def json(self):
        return {
            'name': self.name,
            'country': self.country,
            'language': self.language,
            'url': self.url,
            'categories': [category.json for category in self.categories.all()]
        }


class User(AbstractUser):
    pass
