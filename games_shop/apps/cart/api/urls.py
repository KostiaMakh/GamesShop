from django.urls import path, include
from rest_framework import routers
from cart.api.views import (
    OrderApiView,
)

router = routers.DefaultRouter()
router.register('orders', OrderApiView)

urlpatterns = [
    path('', include(router.urls)),
]
