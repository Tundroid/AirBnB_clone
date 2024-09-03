import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.model = Amenity()
        self.kwargs = {
            'id': 'e49ada22-140b-4f58-8a1d-6af38c5dda19',
            'created_at': '2024-09-03T12:00:00',
            'updated_at': '2024-09-03T12:00:00',
            'name': 'WiFi'
        }

    def test_init_without_kwargs(self):
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertIsInstance(self.model.name, str)

    def test_init_with_kwargs(self):
        model = Amenity(**self.kwargs)
        self.assertEqual(model.name, self.kwargs['name'])

    def test_to_dict(self):
        model_dict = Amenity(**self.kwargs).to_dict()
        self.assertEqual(model_dict['name'], self.kwargs['name'])

if __name__ == '__main__':
    unittest.main()
