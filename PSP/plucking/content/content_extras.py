from django import template
from django.contrib.admin.views.main import PAGE_VAR
from django.utils.html import format_html

register = template.Library()

DOT = "."


@register.simple_tag
def back_url(cl, i):
    """
    Generate url for Back button in admin pagination
    """
    if i == DOT:
        return "… "
    elif cl.page_num > 0:
        return format_html(
            '<a href="{}">{}</a> ',
            cl.get_query_string({PAGE_VAR: cl.page_num - 1}),
            "Back",
        )
    else:
        return ""


@register.simple_tag
def forward_url(cl, i):
    """
    Generate url for Forward button in admin pagination
    """
    if i == DOT:
        return "… "
    elif cl.page_num + 1 < cl.paginator.num_pages:
        return format_html(
            '<a href="{}">{}</a> ',
            cl.get_query_string({PAGE_VAR: cl.page_num + 1}),
            "Forward",
        )
    else:
        return ""