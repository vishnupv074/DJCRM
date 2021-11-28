from django.http import response
from django.test import TestCase
from django.shortcuts import reverse


class LandingPageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse('landing_page'))
        self.assertTemplateUsed(response, 'landing.html')
        self.assertEqual(response.status_code, 200)
