# 🎫 Event Management System - GroupX

## 👥 Group Members

- Name 1 - USN1
- Name 2 - USN2
- Name 3 - USN3
- Name 4 - USN4

## 📌 Project Overview

A RESTful API for managing events, built with Django and Django REST Framework. Core features include:

- Event creation
- Venue assignment
- Organizer management
- Attendee registration
- Ticket generation

## 🧱 Models & Relationships

| Model     | Fields                                                                 |
|-----------|------------------------------------------------------------------------|
| Venue     | name, location, capacity                                               |
| Organizer | user (OneToOne), organization_name                                     |
| Event     | title, description, date, venue (FK), organizer (FK)                   |
| Attendee  | user (OneToOne), events (M2M via Ticket)                               |
| Ticket    | attendee (FK), event (FK), purchase_date                               |

## 🔄 Serializers

Each model has its own serializer. DRF validation is included via serializer fields.

## 🔧 Views/ViewSets

All models are handled using `ModelViewSet` classes with `IsAuthenticatedOrReadOnly` permission to restrict writes.

## 🌐 API URLs

| Endpoint             | Description                |
|----------------------|----------------------------|
| /api/venues/         | CRUD for venues            |
| /api/organizers/     | CRUD for organizers        |
| /api/events/         | CRUD for events            |
| /api/attendees/      | CRUD for attendees         |
| /api/tickets/        | CRUD for tickets           |

## 🧪 API Testing

Tested using Django's `APITestCase`. Covered methods:

- ✅ GET
- ✅ POST
- ✅ PUT
- ✅ DELETE

### Screenshots or logs included in `/tests/` folder or below

## 🚀 Running the Project

```bash
# Setup
pip install -r requirements.txt

# Migrate DB
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver
