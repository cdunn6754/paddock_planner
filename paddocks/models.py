from django.db import models
from django.contrib.postgres.fields import CICharField


class Paddock(models.Model):
    name = CICharField(max_length=100)


class TurnoutPeriod(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    paddock = models.ForeignKey(Paddock, on_delete=models.CASCADE)
