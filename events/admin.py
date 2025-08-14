from django.contrib import admin
from .models import Venue, Organizer, Event, Attendee, Registration

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'capacity')
    list_filter = ('city',)
    search_fields = ('name', 'city')
    ordering = ('name',)

@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
    ordering = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'organizer', 'start_date', 'end_date', 'capacity')
    list_filter = ('venue', 'organizer', 'start_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)
    raw_id_fields = ('venue', 'organizer')

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('attendee', 'event', 'registration_date', 'status')
    list_filter = ('status', 'registration_date', 'event')
    search_fields = ('attendee__first_name', 'attendee__last_name', 'event__title')
    date_hierarchy = 'registration_date'
    ordering = ('-registration_date',)
    raw_id_fields = ('event', 'attendee')