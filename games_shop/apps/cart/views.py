from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from shop.models import Game
from user.models import User
from .models import Order, OrderItem
from .forms import CartAddProductForm, OrderCreateForm
from .cart import Cart
from .wishlist import Wishlist


# cart vies
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Game, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        messages.add_message(request, messages.INFO, f'Good added to cart.')
    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Game, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None

            order = Order.objects.create(
                user=user,
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                address=request.POST['address'],
                postal_code=request.POST['postal_code'],
                city=request.POST['city'],
            )

            for item in cart:
                OrderItem.objects.create(order=order,
                                         game=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                game = Game.objects.get(pk=item['product'].pk)
                game.buys = F('buys') + item['quantity']
                game.save()

            cart.clear()
            return render(request, 'cart/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'cart/order_create.html',
                  {'cart': cart, 'form': form})


# wishlist vies
def wishlist_add(request, product_id):
    wishlist = Wishlist(request)
    wishlist.add(product_id=product_id)
    messages.add_message(request, messages.INFO, f'Game added to wishlist.')
    return redirect(request.META.get('HTTP_REFERER'))


def wishlist_remove(request, product_id):
    wishlist = Wishlist(request)
    wishlist.remove(product_id)

    return redirect(request.META.get('HTTP_REFERER'))


def wishlist_detail(request):
    games = Wishlist(request)

    return render(request, 'cart/wishlist_detail.html', {'games': games})