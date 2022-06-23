from django import template
from shop.models import (
    Genre,
    Company,
    Game,
    Language,
    Device
)

register = template.Library()


@register.inclusion_tag('shop/inc/filters_tpt.html', takes_context=True)
def show_filters(context, menu_class='game_filters', ):

    genres = Genre.objects.filter(pk__in=Game.objects.filter(is_published=True).values('genres'))
    authors = Company.objects.filter(pk__in=Game.objects.filter(is_published=True).values('companies'))
    releases = Game.objects.filter(is_published=True).values('release_year__year').distinct()
    devices = Device.objects.filter(pk__in=Game.objects.filter(is_published=True).values('companies'))
    languages = Language.objects.filter(pk__in=Game.objects.filter(is_published=True).values('languages'))
    actives = context['actives']

    return {
        'genres': genres,
        'releases': releases,
        'authors': authors,
        'devices': devices,
        'languages': languages,
        'menu_class': menu_class,
        'actives': actives,
    }
