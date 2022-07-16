from django import template

register = template.Library()


@register.filter(name='remove_chars')
def remove_chars(value, args):
    for character in args:
        value = value.replace(character, '')
    return value
