from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *


def home(request):
    articles = Article.objects.all()

    return render(request, 'accounts/index.html', {'articles': articles})


@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.')

        return render(request, 'accounts/signin.html')


def logoutUser(request):
    logout(request)
    return redirect('signin')


@unauthenticated_user
def signup(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Акаунт створений. Дякуємо, ' + user)
            return redirect('signin')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required(login_url='login')

def creatArticle(request):
    return None
