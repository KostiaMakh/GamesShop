# Generated by Django 4.0.5 on 2022-06-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Postal code'),
        ),
    ]