from rest_framework import serializers
from .models import Event, Venue, Organizer, Attendee, Ticket
from django.contrib.auth.models import User

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '_all_'


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '_all_'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '_all_'


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '_all_'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '_all_'                