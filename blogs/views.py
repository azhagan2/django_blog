from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Blog, Category


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
