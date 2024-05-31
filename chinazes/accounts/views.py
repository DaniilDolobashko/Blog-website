from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ArticleForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group



def home(request):
    articles = Article.objects.all().order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/index1.html', context)


def front(request):
    articles = Article.objects.filter(category='Frontend').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexF.html', context)


def back(request):
    articles = Article.objects.filter(category='Backend').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexB.html', context)


def design(request):
    articles = Article.objects.filter(category='Design').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexD.html', context)


def other(request):
    articles = Article.objects.filter(category='Other').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexO.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article,
        'author_username': article.author.username if article.author else 'Unknown'  # Отримуємо username автора
    }
    return render(request, 'accounts/article_detail.html', context)


# @unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Додаємо користувача до групи "authors"
            authors_group = Group.objects.get(name='authors')
            if not user.groups.filter(name='authors').exists():
                user.groups.add(authors_group)

            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.')

    return render(request, 'accounts/signin.html')


def logoutUser(request):
    logout(request)
    return redirect('signin')


# @unauthenticated_user
def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Акаунт створений. Дякуємо, ' + user)
            return redirect('signin')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


@allowed_users(allowed_roles=['authors'])
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {'profile': user_profile}
    return render(request, 'accounts/profile_main.html', context)


@allowed_users(allowed_roles=['authors'])
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляємо на головну сторінку у разі успішного додавання статті
        else:
            # Відображення форми з помилками в разі, якщо форма не є валідною
            return render(request, 'accounts/error_main.html', {'form': form})
    else:
        form = ArticleForm()
    return render(request, 'accounts/post.html', {'form': form})


def pass_recovery(request):
    return render(request, 'accounts/passwordupdate.html')


def sich(request):
    articles = Article.objects.filter(category='Design').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexD.html', context)


def lyt(request):
    articles = Article.objects.filter(category='Design').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexD.html', context)


def ber(request):
    articles = Article.objects.filter(category='Design').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexD.html', context)


def kvt(request):
    articles = Article.objects.filter(category='Design').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexD.html', context)


def trv(request):
    articles = Article.objects.filter(category='Design').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexD.html', context)


def chrv(request):
    articles = Article.objects.filter(category='Design').order_by('-date_created')
    context = {
        'articles': articles
    }
    return render(request, 'accounts/indexD.html', context)


def lpn(request):
    return render(request, 'accounts/indexlpn.html')


def srp(request):
    return render(request, 'accounts/indexsrp.html')


def vrs(request):
    return render(request, 'accounts/indexvrs.html')


def zhvt(request):
    return render(request, 'accounts/indexzhvt.html')


def lst(request):
    return render(request, 'accounts/indexlst.html')


def grd(request):
    return render(request, 'accounts/indexgrd.html')

