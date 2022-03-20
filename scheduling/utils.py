from django.conf import settings
import requests
from collections import defaultdict

from scheduling.serializers import TeamupEventSerializer
from horses.models import Horse
from paddocks.models import TurnoutPeriod

TEAMUP_DOMAIN = "https://api.teamup.com/"


def teamup_request(path, **request_args):
    url = TEAMUP_DOMAIN + path
    headers = request_args.pop('headers', {})
    headers['Teamup-Token'] = settings.TEAMUP_API_KEY
    return requests.get(url, headers=headers, **request_args)


def get_teamup_events():
    response = teamup_request('ksom1maeusyfahc1cz/events')
    response.raise_for_status()
    ser = TeamupEventSerializer(data=response.json()['events'], many=True)
    ser.is_valid()
    return ser.validated_data


def get_horse_events():
    """Get the events for today per horse"""
    horse_events = defaultdict(list)
    horse_names = Horse.objects.all().values_list('name', flat=True)
    for event in get_teamup_events():
        title = event['title']
        # Hopefully the horse name is mentioned in the title, space delimited
        overlap = horse_names & set(title.split(' '))
        if len(overlap) == 1:
            horse_events[overlap[0]] = event
        elif not overlap:
            raise TypeError(f"The event title {title} does not include a horse name.")
        else:
            raise TypeError(f"The event title {title} includes more than one horse name.")

    return horse_events


def is_overlap(event, period):
    """Check for an overlap in a horse event and a turnout period"""
    e1, e2 = event['start'], event['end']
    p1, p2 = period.start, period.end

    if e1 > p1 and e1 < p2:
        return True
    if e2 > p1 and e2 < p2:
        return True
    if p1 > e1 and p1 < e2:
        # Seems unlikely, but what if the turnout is a subset of the event
        return True
    return False


def schedule(events, periods):
    """Given a list of horse events and turnout periods, return the scheduled period for each horse"""
    # Map horse name -> period  with paddock name
    assignments = {}
    for horse_name, event in events.items():
        for period in periods:
            # TODO make this waaaaay better
            if getattr(period, 'used', False) or is_overlap(event, period):
                continue
            assignments[horse_name] = period
            period.taken = True
    return assignments
