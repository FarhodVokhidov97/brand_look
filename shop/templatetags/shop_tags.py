from shop.models import *
from django import template

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.all().filter(pk=filter)


@register.inclusion_tag('shop/list_categories.html')
def show_categories(cat_selected=None):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
