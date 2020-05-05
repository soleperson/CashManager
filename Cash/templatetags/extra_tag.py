from django import template
from Cash.models import Cash

register = template.Library()


@register.simple_tag
def all_item():
    return Cash.objects.all()