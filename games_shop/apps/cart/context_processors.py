from .cart import Cart
from .wishlist import Wishlist


def cart_gb(request):
    return {'cart_gb': Cart(request=request)}


def wishlist_gb(request):
    return {'wishlist_gb': Wishlist(request=request)}