from django.conf import settings
import requests

from paddock_planner.serializers import TeamupEventSerializer

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
