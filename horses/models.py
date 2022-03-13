from django.db import models
from django.contrib.postgres.fields import CICharField


class Horse(models.Model):
    name = CICharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
