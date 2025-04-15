from django.shortcuts import render, get_object_or_404
from .models import Event
from django.utils import timezone

def event_list(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now().date())
    return render(request, 'events/event_list.html', {'events': upcoming_events})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'events/event_detail.html', {'events': event})