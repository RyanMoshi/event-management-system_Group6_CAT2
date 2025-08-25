from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenueViewSet, OrganizerViewSet, EventViewSet, AttendeeViewSet, TicketViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet)
router.register(r'organizers', OrganizerViewSet)
router.register(r'events', EventViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
