from rest_framework import decorators, response

from paddock_planner.utils import get_teamup_events


@decorators.api_view(['get'])
def teamup_events_view(request):
    events = get_teamup_events()
    return response.Response(data=events)
