from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value, capitalized_chars_count=1):
    return value[:capitalized_chars_count].upper() + value[capitalized_chars_count+1:].lower()