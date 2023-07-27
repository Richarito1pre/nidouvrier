from django import template

register = template.Library()

@register.filter
def month_name(date):
    months = [
        '', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
        'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
    ]
    return months[date.month]
