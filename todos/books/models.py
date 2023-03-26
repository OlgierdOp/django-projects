from django.db import models
from common.models import Timestamped


# Create your models here.

class AuthorProfile(models.Model):
    author = models.OneToOneField('books.Author', on_delete=models.CASCADE)
    notes = models.TextField()
    birth_year = models.IntegerField()
    death_year = models.IntegerField(null=True, blank=True)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self): return f"{self.first_name} {self.last_name}"


class Book(Timestamped):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    year = models.SmallIntegerField()
    cover = models.ImageField(upload_to="books/covers/%Y/%m/", blank=True, null=True)
    tags = models.ManyToManyField("tags.Tag", related_name="books", blank=True)

    def __str__(self):
        return f"{self.title} ({self.author})"
