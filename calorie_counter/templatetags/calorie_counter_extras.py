
__Author = 'shj4742'
from django import template
from django.utils.html import format_html
register = template.Library()

@register.filter
def shj_upper(val):
    print('var from template:', val)
    return val.upper()


@register.simple_tag
def circle_page(curr_page, loop_page):
    offset = abs(curr_page-loop_page)
    if offset < 5:
        if curr_page == loop_page:
            page_ele ='<li class="active"><a href="?page=%s">%s</a></li>'% (loop_page, loop_page)
        else:
            page_ele = '<li><a href="?page=%s">%s</a></li>'%(loop_page, loop_page)
        return format_html(page_ele)
    return ''
