from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Venue

class VenueAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.client.login(username='testuser', password='pass')
        self.venue_data = {'name': 'Test Hall', 'location': 'City Center', 'capacity': 500}
        self.response = self.client.post(reverse('venue-list'), self.venue_data)

    def test_create_venue(self):
        self.assertEqual(self.response.status_code, 201)

    def test_get_venues(self):
        response = self.client.get(reverse('venue-list'))
        self.assertEqual(response.status_code, 200)

    def test_update_venue(self):
        venue_id = self.response.data['id']
        response = self.client.put(reverse('venue-detail', args=[venue_id]), {
            'name': 'Updated Hall', 'location': 'New City', 'capacity': 600
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_venue(self):
        venue_id = self.response.data['id']
        response = self.client.delete(reverse('venue-detail', args=[venue_id]))
        self.assertEqual(response.status_code, 204)