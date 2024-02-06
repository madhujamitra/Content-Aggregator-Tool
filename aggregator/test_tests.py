class AggregationTestCase(TestCase):
    def setUp(self):
        Aggregation.objects.create(name='Test Aggregation')

    def test_aggregation_list_view(self):
        response = self.client.get(reverse('aggregation_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Aggregation')

    def test_aggregation_detail_view(self):
        aggregation = Aggregation.objects.get(name='Test Aggregation')
        response = self.client.get(reverse('aggregation_detail', args=[aggregation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Aggregation')