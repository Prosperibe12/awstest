from rest_framework.test import APITestCase
from rest_framework import status
from django.shortcuts import reverse

class HealthCheckTest(APITestCase):
  
  def setUp(self):
    self.health_url = reverse('health-check')
    return super().setUp()
  
  def test_health_check(self):
    respose = self.client.get(self.health_url)
    self.assertEqual(respose.status_code, status.HTTP_200_OK)