# Generated by Django 4.0.5 on 2022-06-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=128),
        ),
    ]
