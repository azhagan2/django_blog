from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect

from .models import Blog, Category, Comment
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

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment = comment_text
        comment.save()
        return HttpResponseRedirect(request.path_info)  # Redirect to the same page to prevent form resubmission
    # comments
    comments = Comment.objects.filter(blog=single_post).order_by('created_at')
    comment_count = comments.count()
    print(comments)
    context = {
        'single_post': single_post,
        'comments': comments, 
        'comment_count': comment_count
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

