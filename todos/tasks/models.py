from django.db import models

class Todo(models.Model):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    description = models.TextField(verbose_name="Opis")
    done = models.BooleanField(default=False)
    group = models.CharField(max_length=10, choices=[("public", "public"), ("private", "private")])

    def __str__(self):
        return f"({self.id}) {self.title} {self.group}"