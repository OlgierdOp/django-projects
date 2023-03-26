# Generated by Django 4.1.6 on 2023-02-25 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_author_authorprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="new_author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="books.author",
            ),
        ),
    ]
