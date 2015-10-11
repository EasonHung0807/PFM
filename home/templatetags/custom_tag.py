from django import template
from django.utils.translation import to_locale, get_language

register = template.Library()

@register.filter
def keyvalue(dict, key):
    try:
        return dict[key]
    except KeyError:
        return ''
