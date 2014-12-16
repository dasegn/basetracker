# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter
def overload(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        value = 0

    if value >= 0 and value <= 50:
        return 'danger'
    elif value >= 51 and value <= 75:
        return 'warning'
    elif value >= 76 and value <= 100:
        return 'success'
    else:
        return 'danger'	
