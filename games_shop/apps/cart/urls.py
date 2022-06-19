from django.contrib import admin
from django.urls import path, include
from .views import (
    cart_add,
    cart_detail,
    cart_remove,
    order_create,
    wishlist_add,
    wishlist_remove,
    wishlist_detail,
)

urlpatterns = [
    path(r'^$', cart_detail, name='cart_detail'),
    path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
    path(r'^create/$', order_create, name='order_create'),
    path(r'^add-wish/<int:product_id>/', wishlist_add, name='wishlist_add'),
    path(r'^remove-wish/<int:product_id>/', wishlist_remove, name='wishlist_remove'),
    path('^wishlist/', wishlist_detail, name='wishlist_detail')
]
