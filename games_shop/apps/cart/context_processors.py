from django.db.models import Sum

from .cart import Cart
from shop.models import Game
from user.models import User, Basket


def cart_gb(request):
    if request.user.is_authenticated:
        goods_quantity= Basket.objects.filter(user=request.user).aggregate(cart=Sum('quantity'))
        return {'cart_gb': goods_quantity['cart']}
    else:
        return {'cart_gb': len(Cart(request=request))}


def wishlist_gb(request):
    if request.user.is_authenticated:
        wishlist = Game.objects.filter(pk__in=User.objects.filter(pk=request.user.pk).values('wishlist'))
        return {'wishlist_gb': wishlist}
    else:
        return {'wishlist_gb': {}}
