from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self): return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='book', blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): return f"{self.title}"
