from django.shortcuts import render

from blogs.models import Category, Blog
from assignments.models import About

from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib import auth


def home(request):
    featured_post = Blog.objects.filter(is_featured=True, status='Publish').order_by('created_at')
    posts = Blog.objects.filter(is_featured=False, status='Publish').order_by('created_at')
    print(posts)

    try:
        about = About.objects.first()
    except:
        about = None
    context = {
        'featured_post': featured_post,
        'posts': posts,
        'about': about
    }
    return render(request, 'home.html', context)

def search(request):
    return render(request, 'search.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form= RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                print(f"User {username} authenticated successfully!")
                auth.login(request, user)
            return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('login')


