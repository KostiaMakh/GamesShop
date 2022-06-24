from rest_framework import serializers
from cart.models import (
    Order,
    OrderItem
)
from shop.models import Game
from user.models import User


class OrderGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'poster',
        )


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'name',
            'surname',
        )


class OrderItemSerializer(serializers.ModelSerializer):
    game = serializers.SerializerMethodField()

    def get_game(self, obj):
        game = Game.objects.get(pk=obj.game.pk)
        serializer = OrderGameSerializer(
            game,
            many=False
        )

        return serializer.data

    class Meta:
        model = OrderItem
        exclude = ('order',)


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_order_items(self, obj):
        items = OrderItem.objects.filter(
            order_id=obj.id
        )
        serializer = OrderItemSerializer(
            items,
            many=True
        )

        return serializer.data

    def get_user(self, obj):
        if obj.user:
            user = User.objects.get(
                pk=obj.user.pk
            )
            serializer = OrderUserSerializer(
                user,
                many=False
            )

            return serializer.data

    class Meta:
        model = Order
        fields = serializers.ALL_FIELDS


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = (
            'id'
            'status',
            'created_at',
            'updated_at',
        )
