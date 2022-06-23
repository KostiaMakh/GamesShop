from django.db import models
from shop.models import Game
from user.models import User

ORDER_STATUS = (
    ('a', "Created"),
    ('b', "Confirm"),
    ('c', "Package"),
    ('d', "Delivery"),
    ('e', "Done")
)


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='orders'
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    phone = models.CharField(
        max_length=128,
        default=''
    )
    address = models.CharField(max_length=256)
    postal_code = models.PositiveIntegerField()
    city = models.CharField(max_length=128)
    status = models.CharField(
        max_length=256,
        choices=ORDER_STATUS,
        default="Created"
    )
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.pk)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    game = models.ForeignKey(
        Game,
        related_name='order_items',
        on_delete=models.PROTECT
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.pk)

    def get_cost(self):
        return self.price * self.quantity
