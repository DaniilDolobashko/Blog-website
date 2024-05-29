from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    username = models.CharField(max_length=50, null=True)
    fullName = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=3, null=True)
    country = models.CharField(max_length=50, null=True)
    phoneNumber = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username


class Article(models.Model):
    CATEGORY = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Data science', 'Data science'),
    )

    name = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

