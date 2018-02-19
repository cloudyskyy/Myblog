from ..models import Post,Category
from django import template

register=template.Library()

@register.simple_tag
def getRecentPosts(num=5):
    return Post.objects.all().order_by('-createdTime')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('createdTime','month',order='DESC')

@register.simple_tag
def getCategories():
    return Category.objects.all()