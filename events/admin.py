from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Venue, Organizer, Event, Attendee, Ticket

admin.site.register(Venue)
admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Ticket)
