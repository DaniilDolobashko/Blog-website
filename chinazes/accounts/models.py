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
        ('Design', 'Design'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    age = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username