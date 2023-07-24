# Generated by Django 4.1.3 on 2023-04-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_cart_temp_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='shop.CartItem', to='shop.item'),
        ),
    ]
