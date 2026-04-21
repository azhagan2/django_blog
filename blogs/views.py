from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Blog, Category
from django.db.models import Q


def posts_by_category(request, category_id):
    # Fetch posts based on the category_id with id
    posts = Blog.objects.filter(category_id=category_id, status='Publish').order_by('created_at')
    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     return redirect('home')
    category = get_object_or_404(Category, id=category_id)

    context = {
        'posts': posts,
        'category': category
    }

    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_post = get_object_or_404(Blog, slug=slug, status='Publish')
    context = {
        'single_post': single_post
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('Keyword')
    print(keyword)
    if keyword:
        search_results = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Publish').order_by('created_at')
        print(search_results)
    else:
        search_results = Blog.objects.none()

    context = {
        'blogs' : search_results,
        'keyword': keyword
    }
    return render(request, 'search.html', context)
