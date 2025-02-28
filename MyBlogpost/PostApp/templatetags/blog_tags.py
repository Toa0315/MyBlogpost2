from django import template
from PostApp.models import Post

register = template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()

@register.inclusion_tag('show_latest_post.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-created')[:count]
    return {'latest_posts': latest_posts}
