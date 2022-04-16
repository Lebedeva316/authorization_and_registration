from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Article(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    ARtext = models.TextField()

    data = models.DateTimeField()

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.ARtext}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

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

class User(models.Model):

    AuthorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return f'/profile/{self.id}'