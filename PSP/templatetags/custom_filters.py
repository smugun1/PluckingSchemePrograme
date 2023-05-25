from django import template
register = template.Library()


@register.filter(name='get_by_index')
def get_by_index(value, index):
    if isinstance(value, list) and len(value) > index:
        return value[index]
    return None
