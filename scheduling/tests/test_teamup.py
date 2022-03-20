from datetime import time, timedelta
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

from horses.factories import HorseFactory
from paddocks.factories import PaddockFactory, TurnoutPeriodFactory
from scheduling import utils


class TeamUp(TestCase):

    def test_get_events(self):
        """We can call the teamup api"""
        response = self.client.get(reverse('scheduling:event-list'))
        assert response.status_code == 200


class Schedule(TestCase):
    def test_schedule_happy(self):
        """Given horses and paddocks for them, produce a schedule"""
        t1, t2, t3 = time(hour=7, minute=30), time(hour=10), time(hour=13, minute=30)
        horse_1 = HorseFactory()
        horse_2 = HorseFactory()
        pad = PaddockFactory()
        periods = [
            TurnoutPeriodFactory(paddock=pad, start=t1, end=t2),
            TurnoutPeriodFactory(paddock=pad, start=t2, end=t3)
        ]
        horse_events = {
            horse_1.name: {'title': horse_1.name, 'start': time(hour=8), 'end': time(hour=8, minute=45)},
            horse_2.name: {'title': horse_2.name, 'start': time(hour=11), 'end': time(hour=11, minute=45)}
        }
        schedule = utils.schedule(horse_events, periods)
        assert schedule[horse_1.name] == periods[1]
        assert schedule[horse_2.name] == periods[0]
        assert len(schedule.keys()) == 2
