from django.db import models


class Horse(models.Model):
    name = models.CharField(max_length=50)
