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
    """ Test class for Location model """
    url = reverse("locations:v1_list_create_location")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        """ Creates a location factory and tests the api location list """
        LocationFactory()

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        """ Test Creates a new location """
        data = {
            "name": "Urbvan",
            "coordinates": "19.588401,-99.297358"
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


class StationCreateTest(APITestCase):
    """ Test class for Station model """
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
        """ Creates a station factory and tests the api station list """
        StationFactory()
        response = self.client.get(self.url_list)
        response = response.json()

        self.assertEquals(len(response), 1)

    def test_create_successfully(self):
        """ Tests creation of a station (mocks up a location) """
        location = LocationFactory()
        data = {
            "order": 1,
            "is_active": True,
            "location": location.id
        }

        response = self.client.post(self.url_create, data,  format='json')
        self.assertEquals(response.status_code, 201)

    def test_detail_successfully(self):
        """ Tests the retrieve detail of a Station """
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
        """ Tests a delete station """
        self.user = UserSuperUserFactory()
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

        url = str(self.url_delete).replace('pk', data['pk'])
        response = self.client.delete(url, data, format='json')
        self.assertEquals(response.status_code, 204)

        url = str(self.url_detail).replace('pk', data['pk'])
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.status_code, 404)
