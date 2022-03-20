from django.urls import path

from scheduling import views

app_name = 'scheduling'

urlpatterns = [
    path('event-list/', views.teamup_events_view, name='event-list'),
]
