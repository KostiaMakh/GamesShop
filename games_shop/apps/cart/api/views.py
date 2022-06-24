from rest_framework import viewsets
from cart.models import (
    Order,
)
from cart.api.serializers import (
    OrderSerializer,
    OrderCreateSerializer
)


class OrderApiView(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrderSerializer
        else:
            return OrderCreateSerializer
