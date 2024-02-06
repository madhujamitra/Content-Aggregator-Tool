from django.test import TestCase
from django.urls import reverse

class LandingPageTests(TestCase):
    def test_landing_page_status_code(self):
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)

    def test_landing_page_template(self):
        response = self.client.get(reverse('landing_page'))
        self.assertTemplateUsed(response, 'index.html')

    def test_landing_page_contains_correct_html(self):
        response = self.client.get(reverse('landing_page'))
        self.assertContains(response, 'Welcome to')

    def test_landing_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('landing_page'))
        self.assertNotContains(response, 'Hi there! I should not be on the page.')