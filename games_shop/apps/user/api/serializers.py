from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer
from user.models import User, Basket
from shop.models import Game
from cart.models import Order


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'id',
            'slug',
            'poster',
            'title',
            'price'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'created_at',
            'paid'
        )


class BasketSerializer(serializers.ModelSerializer):
    game = GameDetailSerializer(many=False)

    class Meta:
        model = Basket
        fields = (
            'game',
            'quantity'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    wishlist = GameDetailSerializer(many=True)
    basket = BasketSerializer(many=True)
    orders = OrderSerializer(many=True)

    class Meta:
        model = User
        fields = serializers.ALL_FIELDS


class CustomAuthTokenSerializer(AuthTokenSerializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password
            )
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(
                    msg,
                    code='authorization'
                )
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(
                msg,
                code='authorization'
            )

        attrs['user'] = user
        return attrs
