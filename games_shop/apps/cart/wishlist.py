from decimal import Decimal
from django.conf import settings
from shop.models import Game


class Wishlist(object):

    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)
        if not wishlist:
            # save an empty wishlist in the session
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = [0, ]
        self.wishlist = wishlist

    def add(self, product_id):
        """
        Add product into wishlist
        """
        if product_id not in self.wishlist:
            self.wishlist.append(product_id)
        self.save()

    def save(self):
        self.session[settings.WISHLIST_SESSION_ID] = self.wishlist
        self.session.modified = True

    def remove(self, product_id):
        """
        Remove product from wishlist
        """
        if product_id in self.wishlist:
            self.wishlist.remove(product_id)
            self.save()

    def clear(self):
        # Remove wishlist from session
        del self.session[settings.WISHLIST_SESSION_ID]
        self.session.modified = True

    def __len__(self):
        """
        Count of all products in cart.
        """
        return len(self.wishlist)

    def __str__(self):
        """
        Count of all products in cart.
        """
        return self.wishlist

    def __iter__(self):
        product_ids = self.wishlist
        products = Game.objects.filter(id__in=product_ids)
        for product in products:
            yield product

        # for product in products:
        #     self.cart[str(product.id)]['product'] = product
