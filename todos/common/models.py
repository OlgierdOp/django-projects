from django.db import models
from .mixins import CheckAgeMixin, LastModifiedMixin

class Timestamped(models.Model, CheckAgeMixin, LastModifiedMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True