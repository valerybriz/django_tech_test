# coding: utf8
from django.urls import reverse

from rest_framework.test import APITestCase

from apps.users.factories import (
    UserFactory,
    UserSuperUserFactory,
    UserAdminFactory,
    TokenFactory,
)
from .factories import LocationFactory, StationFactory


class LocationCreateTest(APITestCase):

    url = reverse("locations:v1_list_create_location")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        LocationFactory()

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": "Urbvan",
            "coordinates": "19.388401,-99.227358"
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


class StationCreateTest(APITestCase):

    url_detail = reverse("stations:stations-detail", kwargs={'pk': 'pk'})
    url_delete = reverse("stations:stations-delete", kwargs={'pk': 'pk'})
    url_list = reverse("stations:stations-list")
    url_create = reverse("stations:stations-create")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(
            AUTHORIZATION=f"Urbvan {self.user_token.key}"
        )

    def test_list(self):
        StationFactory()

        response = self.client.get(self.url_list)
        response = response.json()

        self.assertEquals(len(response), 1)

    def test_create_successfully(self):
        # StationFactory()
        location = LocationFactory()
        data = {
            "order": 1,
            "is_active": True,
            "location": location.id
        }

        response = self.client.post(self.url_create, data,  format='json')
        self.assertEquals(response.status_code, 201)

    def test_detail_successfully(self):
        self.user = UserAdminFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            AUTHORIZATION=f"Urbvan {self.user_token.key}"
        )
        station = StationFactory()
        data = {
            'pk': station.id
        }
        url = str(self.url_detail).replace('pk', data['pk'])
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.status_code, 200)

    def test_delete_successfully(self):

        self.user = UserSuperUserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(
            AUTHORIZATION=f"Urbvan {self.user_token.key}"
        )
        station = StationFactory()
        data = {
            'pk': station.id
        }

        # Get with success the element
        url = str(self.url_detail).replace('pk', data['pk'])
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.status_code, 200)

        # Delete element and check
        url = str(self.url_delete).replace('pk', data['pk'])
        response = self.client.delete(url, data, format='json')
        self.assertEquals(response.status_code, 204)

        # Not found element
        url = str(self.url_detail).replace('pk', data['pk'])
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.status_code, 404)
