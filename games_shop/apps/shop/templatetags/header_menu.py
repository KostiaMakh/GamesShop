from django import template
from shop.models import Genre, Company, Game
from django.db.models import F, Count

register = template.Library()


@register.inclusion_tag('shop/inc/header_menu_tpt.html', takes_context=True)
def show_menu(context, menu_class='header_menu'):
    genres = Genre.objects.filter(pk__in=Game.objects.filter(is_published=True).values('genres'))
    companies = Company.objects.filter(pk__in=Game.objects.filter(is_published=True).values('companies'))
    user = context['user']

    return {
        'genres': genres,
        'companies': companies,
        'user': user,
        'menu_class': menu_class
    }
