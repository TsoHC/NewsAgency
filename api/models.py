from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Story(models.Model):
    CATEGORIES = [
        ('pol', 'Politics'),
        ('art', 'Art'),
        ('tech', 'Technology'),
        ('trivia', 'Trivial')
    ]

    REGIONS = [
        ('uk', 'United Kingdom'),
        ('eu', 'European Union'),
        ('w', 'World')
    ]

    headline = models.CharField(max_length=64)
    category = models.CharField(max_length=64, choices=CATEGORIES)
    region = models.CharField(max_length=64, choices=REGIONS)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=128)

    def __str__(self):
        return self.headline
