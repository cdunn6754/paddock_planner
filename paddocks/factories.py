import factory
from paddocks import models


class PaddockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Paddock

    name = factory.sequence(lambda idx: f"Paddock {idx}")


class TurnoutPeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TurnoutPeriod

