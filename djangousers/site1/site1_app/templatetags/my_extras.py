from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value, arg):
    # Cuts all of values of 'arg'
    return value.replace(arg, 'fdfdfdfdfdfdfdf')