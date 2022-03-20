import factory
from horses import models


class HorseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Horse

    name = factory.sequence(lambda idx: f"Horse {idx}")
