from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    phone = forms.CharField(max_length=50)
    age = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'gender', 'age', 'phone', 'email', 'password1', 'password2']

