from django.test import TestCase, RequestFactory
from .views import entity_list
from .models import Entity


class EntityListTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.entity_data = {
            'name': 'Test Entity',
            'description': 'This is a test entity'
        }

    def test_entity_list_GET(self):
        # Create some entities
        Entity.objects.create(name='Entity 1', description='Description 1')
        Entity.objects.create(name='Entity 2', description='Description 2')

        # Make a GET request to the view
        request = self.factory.get('/entities/')
        response = entity_list(request)
        print(response.body)
        # Check that the response contains the entities
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.data), 2)
        # self.assertEqual(response.data[0]['name'], 'Entity 1')
        # self.assertEqual(response.data[1]['name'], 'Entity 2')
