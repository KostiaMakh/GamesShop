from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager


@receiver(user_logged_in)
def create_auth_token(request, user, **kwargs):
    # Add token for user if he's "staff"
    if user.is_staff:
        Token.objects.get_or_create(user=user)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True,
                          unique=True)
    email = models.EmailField(max_length=128,
                              unique=True)
    phone = models.CharField(max_length=256,
                             blank=True,
                             default='')
    gender = models.CharField(max_length=50,
                              choices=(
                                  ('M', 'Mail'),
                                  ('F', 'Femail'),),
                              blank=True
                              )
    name = models.CharField(max_length=256,
                            blank=True,
                            default='', )
    surname = models.CharField(max_length=256,
                               blank=True,
                               default='')
    birthday = models.DateField(blank=True,
                                default='1991-10-10')
    city = models.CharField(max_length=256,
                            blank=True,
                            default='')
    address = models.CharField(max_length=256,
                               blank=True,
                               default='')
    postal_code = models.PositiveIntegerField(blank=True,
                                              default=0,
                                              verbose_name='Postal code')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
