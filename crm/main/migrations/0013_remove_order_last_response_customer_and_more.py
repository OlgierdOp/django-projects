# Generated by Django 5.0.1 on 2024-02-04 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_order_last_response_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='last_response_customer',
        ),
        migrations.CreateModel(
            name='OrderResponseControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['response_date'],
            },
        ),
    ]
