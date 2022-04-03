from django.db import models
from django.core.validators import MinValueValidator

class Article(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    ARtext = models.TextField()

    data = models.DateTimeField()

    def __str__(self):
        return f'{self.name}: {self.ARtext}'

class Author(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    def __str__(self):
        return self.name.title()

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    def __str__(self):
        return self.name.title()