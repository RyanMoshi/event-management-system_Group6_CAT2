from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=100)

    def __str__(self):
        return self.organization_name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    ticket_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Ticket for {self.attendee.user.username} - {self.event.title}"


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name
