from django.shortcuts import render

from blogs.models import Category, Blog
from assignments.models import About, SocialMedia


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
