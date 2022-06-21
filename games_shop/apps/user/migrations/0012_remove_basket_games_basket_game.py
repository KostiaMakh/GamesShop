# Generated by Django 4.0.5 on 2022-06-20 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_game_status'),
        ('user', '0011_basket_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='games',
        ),
        migrations.AddField(
            model_name='basket',
            name='game',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.game'),
        ),
    ]
