from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from shop.models import Game


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(
        primary_key=True,
        unique=True
    )
    email = models.EmailField(
        max_length=128,
        unique=True
    )
    phone = models.CharField(
        max_length=256,
        blank=True,
        default=''
    )
    gender = models.CharField(
        max_length=50,
        choices=(
            ('M', 'Mail'),
            ('F', 'Femail'),),
        blank=True
    )
    name = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    surname = models.CharField(
        max_length=256,
        blank=True,
        default=''
    )
    birthday = models.DateField(
        blank=True,
        default='1991-10-10'
    )
    city = models.CharField(
        max_length=256,
        blank=True,
        default=''
    )
    address = models.CharField(
        max_length=256,
        blank=True,
        default=''
    )
    postal_code = models.PositiveIntegerField(
        blank=True,
        default=0,
        verbose_name='Postal code'
    )
    wishlist = models.ManyToManyField(Game)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Basket(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='basket'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        default=None
    )
    quantity = models.PositiveSmallIntegerField(default=1)
