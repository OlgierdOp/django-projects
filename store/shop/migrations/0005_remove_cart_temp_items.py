# Generated by Django 4.1.3 on 2023-04-11 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_items_cart_temp_items_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='temp_items',
        ),
    ]
