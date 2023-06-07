from django import template

register = template.Library()


@register.filter(name='get_by_index')
def get_by_index(value, index):
    if isinstance(value, list) and len(value) > index:
        return value[index]
    return None


from django import template

register = template.Library()


@register.filter(name='get_dynamic_field')
def get_dynamic_field(data, day):
    field_name = f"Month_day_{day}"
    return getattr(data, field_name, "-")


from django import template

register = template.Library()


@register.filter
def get_attribute(obj, attr):
    return getattr(obj, attr, '')


from django import template

register = template.Library()


@register.filter
def num_range(value):
    return range(value)


from django import template

register = template.Library()


@register.filter
def to_int(value):
    return int(value)


from django import template

register = template.Library()


@register.filter
def create_range(value):
    return range(value)


from django.template.defaulttags import register


@register.filter
def subtract(value, arg):
    return value - arg


from django import template

register = template.Library()


@register.filter
def get_range(value):
    return range(value)


from django import template

register = template.Library()


@register.filter
def startswith(text, prefix):
    return text.startswith(prefix)


from django import template

register = template.Library()


@register.filter
def modulo(value, arg):
    return value % arg


from django import template

register = template.Library()


@register.filter
def mod(value, arg):
    return value % arg
