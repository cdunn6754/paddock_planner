from django.test import TestCase
from django.urls import reverse


class TeamUp(TestCase):

    def test_get_events(self):
        """We can call the teamup api"""
        response = self.client.get(reverse('teamup-events'))
        assert response.status_code == 200
