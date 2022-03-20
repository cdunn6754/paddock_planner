from django.urls import path

from scheduling import views

app_name = 'scheduling'

urlpatterns = [
    path('event-list/', views.get_teamup_events, name='event-list'),
]
