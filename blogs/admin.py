from django.contrib import admin
from .models import Blog, Category, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured')
    search_fields = ('title', 'author__username', 'category__category_name', 'status')
    list_editable = ('status', 'is_featured')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
