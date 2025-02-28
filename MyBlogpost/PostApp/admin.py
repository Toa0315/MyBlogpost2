from django.contrib import admin
from .models import Post, Comment  # Import your models

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    search_fields = ('name', 'email', 'body')
    list_filter = ('active', 'created')
