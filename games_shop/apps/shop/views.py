from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F, Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Game,
    Genre,
    Promo,
    Company,
    Device,
    Language,
    ScreenShot,
)
from .forms import GameCreationForm
from cart.forms import CartAddProductForm


class MainPage(ListView):
    model = Game
    template_name = 'shop/index.html'
    context_object_name = 'games'
    extra_context = {
        'genres': Genre.objects.annotate(cat=Count('game', filter=F('game__id'))).filter(cat__gt=0),
        # 'devices': Device.objects.annotate(cat=Count('game', filter=F('game__id'))).filter(cat__gt=0),
        'promos': Promo.objects.filter(is_active=True),
        'companies': Company.objects.all()
    }

    def get_queryset(self):
        return Game.objects.filter(is_published=True).order_by('-created_at')[:3]


class GamesPage(ListView):
    template_name = 'shop/games.html'
    context_object_name = 'games'
    paginate_by = 9

    def get_queryset(self):
        return Game.objects.filter(is_published=True).order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actives'] = {}

        return context


class GenrePage(ListView):
    template_name = 'shop/genre.html'
    context_object_name = 'games'
    paginate_by = 9

    def get_queryset(self):
        return Game.objects.filter(genres__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.get(slug=self.kwargs['slug'])
        return context


class CompanyPage(ListView):
    template_name = 'shop/company.html'
    context_object_name = 'games'
    paginate_by = 9

    def get_queryset(self):
        return Game.objects.filter(companies__slug=self.kwargs['slug'], is_published=True)
        # return Company.objects.get(slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(slug=self.kwargs['slug'])
        return context


class GenresList(ListView):
    model = Genre
    template_name = 'shop/index.html'
    context_object_name = 'genres'


class GameDetail(DetailView):
    model = Game
    template_name = 'shop/game_card.html'
    context_object_name = 'game'

    def get_queryset(self):
        return Game.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['screen_shots'] = ScreenShot.objects.filter(game_id__slug=self.kwargs['slug'])
        context['languages'] = Language.objects.filter(game__slug=self.kwargs['slug'])
        context['devices'] = Device.objects.filter(game__slug=self.kwargs['slug'])
        context['cart_product_form'] = CartAddProductForm()
        return context


class FilterGames(ListView):
    template_name = 'shop/games.html'
    context_object_name = 'games'

    def get_queryset(self):
        queryset = Game.objects.filter(is_published=True)

        if self.request.GET.getlist('genres'):
            queryset = queryset.filter(Q(genres__slug__in=self.request.GET.getlist('genres')))

        if self.request.GET.getlist('years'):
            queryset = queryset.filter(Q(release_year__year__in=self.request.GET.getlist('years')))

        if self.request.GET.getlist('authors'):
            queryset = queryset.filter(Q(companies__slug__in=self.request.GET.getlist('authors')))

        if self.request.GET.getlist('devices'):
            queryset = queryset.filter(Q(devices__slug__in=self.request.GET.getlist('devices')))

        if self.request.GET.getlist('languages'):
            queryset = queryset.filter(Q(languages__slug__in=self.request.GET.getlist('languages')))

        queryset = queryset.distinct()

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        years = [int(x) for x in self.request.GET.getlist('years')]
        context['cart_product_form'] = CartAddProductForm()
        context['actives'] = {
            'genres': self.request.GET.getlist('genres'),
            'years': years,
            'authors': self.request.GET.getlist('authors'),
            'devices': self.request.GET.getlist('devices'),
            'languages': self.request.GET.getlist('languages'),

        }

        return context


class CreateGame(LoginRequiredMixin, CreateView):
    template_name = 'shop/game_creation.html'
    form_class = GameCreationForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
