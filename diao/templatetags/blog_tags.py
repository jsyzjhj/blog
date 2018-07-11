from ..models import Post,Category
from django import template

register=template.Library()
@register.simple_tag
def get_recent_posts(num=5):
    obj=Post.objects.all().order_by('-create_time')[:num]
    return obj

@register.simple_tag
def archives():
    obj=Post.objects.dates('create_time', 'month',order='DESC')

@register.simple_tag
def get_categories():
    obj=Category.objects.all()
    return obj
