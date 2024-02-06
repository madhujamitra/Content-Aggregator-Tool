from django.test import TestCase
from django.urls import reverse
from .models import aggregation

class aggregationTestCase(TestCase):
    def setUp(self):
        aggregation.objects.create(title='Test aggregation', url='https://www.freecodecamp.org/news/python-projects-for-beginners/', source='Example News')

    def test_aggregation_list_view(self):
        response = self.client.get(reverse('aggregation_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test aggregation')

    def test_aggregation_detail_view(self):
        aggregation = aggregation.objects.get(title='Test aggregation')
        response = self.client.get(reverse('aggregation_detail', args=[aggregation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test aggregation')
        self.assertContains(response, 'https://www.freecodecamp.org/news/python-projects-for-beginners/')
        # self.assertContains(response, 'Example News')