from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Article

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES, required=False)
    age = forms.IntegerField(required=False)
    country = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=15, required=False)
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'gender', 'age', 'country', 'phone', 'profile_photo', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
            user.profile.first_name = self.cleaned_data['first_name']
            user.profile.gender = self.cleaned_data['gender']
            user.profile.age = self.cleaned_data['age']
            user.profile.country = self.cleaned_data['country']
            user.profile.phone_number = self.cleaned_data['phone']
            user.profile.profile_photo = self.cleaned_data['profile_photo']
            user.profile.save()
        return user


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text', 'category', 'author']