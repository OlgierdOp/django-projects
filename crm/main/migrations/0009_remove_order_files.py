# Generated by Django 5.0.1 on 2024-02-02 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_file_order_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='files',
        ),
    ]
