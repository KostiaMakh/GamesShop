# Generated by Django 4.0.5 on 2022-06-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_game_buys_alter_game_old_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='old_price',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
    ]
