# Generated by Django 4.1.6 on 2023-02-26 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0001_initial"),
        ("books", "0008_book_cover"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="books", to="tags.tag"
            ),
        ),
    ]
