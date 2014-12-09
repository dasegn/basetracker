#-*- coding: utf-8 -*-
from decimal import Decimal


def truncate_text(value, limit=80):
    """
    Truncates a string after a given number of chars keeping whole words.    
    Usage:
        {{ string|truncate_text }}
        {{ string|truncate_text:50 }}
    """
    
    try:
        limit = int(limit)
    # invalid literal for int()
    except ValueError:
        # Fail silently.
        return value
    
    # Make sure it's unicode
    value = unicode(value)
    
    # Return the string itself if length is smaller or equal to the limit
    if len(value) <= limit:
        return value
    
    # Cut the string
    value = value[:limit]
    
    # Break into words and remove the last
    words = value.split(' ')[:-1]
    
    # Join the words and return
    return ' '.join(words) + '...' 


def get_color_overload(value):
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


def convert_to_decimal(value):
    try:
        return Decimal(value)
    except (ValueError, TypeError):
        return Decimal(0.0)