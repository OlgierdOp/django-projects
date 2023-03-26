# Generated by Django 4.1.6 on 2023-02-25 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_alter_book_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
