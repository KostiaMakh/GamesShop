# Generated by Django 4.0.5 on 2022-06-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('a', 'Created'), ('b', 'Confirm'), ('c', 'Package'), ('d', 'Delivery'), ('e', 'Done')], default='Created', max_length=256),
        ),
    ]