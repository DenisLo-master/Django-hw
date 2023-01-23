from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def google_search(value):
    return mark_safe(f"<a target='_blank'  href='https://www.google.com/search?q={value}'>{value}</a>")
