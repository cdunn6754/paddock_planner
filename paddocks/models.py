from django.db import models
from django.contrib.postgres.fields import CICharField


class Paddock(models.Model):
    name = CICharField(max_length=100, unique=True)


class TurnoutPeriod(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    paddock = models.ForeignKey(Paddock, on_delete=models.CASCADE)

    # TODO add an exclusion constraint for time period overlaps per paddock fk
