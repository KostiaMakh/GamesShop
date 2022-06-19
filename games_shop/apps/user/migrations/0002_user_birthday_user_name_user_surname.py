# Generated by Django 4.0.5 on 2022-06-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default='1991-10-10'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.EmailField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.EmailField(blank=True, default='', max_length=256),
        ),
    ]
