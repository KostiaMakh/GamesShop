from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from shop.models import Game
from user.models import User, Basket
from .models import Order, OrderItem
from .forms import CartAddProductForm, OrderCreateForm
from .cart import Cart


# cart vies
@require_POST
def cart_add(request, product_id):
    game = get_object_or_404(Game, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if request.user.is_authenticated:
            try:
                game_in_basket = Basket.objects.get(
                    user=request.user,
                    game=game)
                game_in_basket.quantity = F('quantity') + cd['quantity']
                game_in_basket.save()

            except:
                Basket.objects.create(
                    user=request.user,
                    game=game,
                    quantity=cd['quantity']
                )
        else:
            cart = Cart(request)
            cart.add(product=game,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])

        messages.add_message(request, messages.INFO, f'Good added to cart.')

    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    if request.user.is_authenticated:
        game = get_object_or_404(Game, id=product_id)
        removed_game = Basket.objects.get(user=request.user,
                                          game=game)
        removed_game.delete()
    else:
        cart = Cart(request)
        product = get_object_or_404(Game, id=product_id)
        cart.remove(product)

    return redirect('cart:cart_detail')


def cart_detail(request):
    if request.user.is_authenticated:
        goods_in_basket = Basket.objects.filter(user=request.user)
        cart = []
        for good in goods_in_basket:
            detail_game = {
                'game': good,
                'total_price': good.game.price * good.quantity
            }
            cart.append(detail_game)

        total_amount = 0
        for item in cart:
            total_amount += item['total_price']
        return render(request, 'cart/cart.html', {'cart': cart, 'total_amount': total_amount})

    else:
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})


def order_create(request):
    total_price = 0
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

            if request.user.is_authenticated:
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             game=item.game,
                                             price=item.game.price,
                                             quantity=item.quantity)

                    game = Game.objects.get(pk=item.game.pk)
                    game.buys = F('buys') + item.quantity
                    game.save()
                    item.delete()

            else:
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             game=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])

                    game = Game.objects.get(pk=item['product'].pk)
                    game.buys = F('buys') + item['quantity']
                    game.save()
                    cart.clear()

            messages.add_message(request, messages.SUCCESS,
                                 f'Congratulations! \n Your order successfully created. \n Our manager contact with you contact you as soon as possible for confirming order ')
            return render(request, 'cart/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm

        if request.user.is_authenticated:
            goods_in_cart = Basket.objects.filter(user=request.user)
            cart = []
            for item in goods_in_cart:
                game_detail = {'game': item,
                               'amount': item.game.price * item.quantity}
                total_price += item.game.price * item.quantity
                cart.append(game_detail)
                print(cart[0])
            return render(request, 'cart/order_create.html',
                          {'cart': cart, 'form': form, 'total_price': total_price})
        else:
            return render(request, 'cart/order_create.html',
                          {'cart': cart, 'form': form})


# wishlist vies
def wishlist_add(request, product_id):
    user = User.objects.get(pk=request.user.pk)
    game = Game.objects.get(pk=int(product_id))
    user.wishlist.add(game)
    user.save()
    messages.add_message(request, messages.INFO, f'Game added to wishlist.')
    return redirect(request.META.get('HTTP_REFERER'))


def wishlist_remove(request, product_id):
    user = User.objects.get(pk=request.user.pk)
    game = Game.objects.get(pk=int(product_id))
    user.wishlist.remove(game)
    user.save()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def wishlist_detail(request):
    return render(request, 'cart/wishlist_detail.html')
