# Generated by Django 4.0.5 on 2022-06-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_game_status'),
        ('user', '0008_user_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(related_name='user_cart', to='shop.game'),
        ),
    ]
