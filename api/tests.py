from api.models import Town

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TownTests(APITestCase):
    def test_list_towns(self):
        """
        Ensure we can only list towns.
        """
        url = reverse('towns-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
