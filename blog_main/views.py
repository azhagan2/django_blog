from django.shortcuts import render

from blogs.models import Category, Blog


def home(request):
    featured_post = Blog.objects.filter(is_featured=True, status='Publish').order_by('created_at')
    posts = Blog.objects.filter(is_featured=False, status='Publish').order_by('created_at')
    print(posts)
    context = {
        'featured_post': featured_post,
        'posts': posts
    }
    return render(request, 'home.html', context)