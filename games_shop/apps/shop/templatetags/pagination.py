from django import template

register = template.Library()


@register.inclusion_tag('shop/inc/pagination_tpt.html', takes_context=True)
def show_pagination(context):
    page_obj = context['page_obj']

    return {
        'page_obj': page_obj,
    }

