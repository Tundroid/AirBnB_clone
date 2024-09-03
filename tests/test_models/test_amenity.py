import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.model = Amenity()

    def test_init_without_kwargs(self):
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertIsInstance(self.model.name, str)

    def test_init_with_kwargs(self):
        kwargs = {
            'id': 'e49ada22-140b-4f58-8a1d-6af38c5dda19',
            'created_at': '2024-09-03T12:00:00',
            'updated_at': '2024-09-03T12:00:00',
            'name': 'WiFi'
        }
        model = Amenity(**kwargs)
        self.assertEqual(model.name, 'WiFi')

    def test_to_dict(self):
        self.model.name = "WiFi"
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['name'], self.model.name)


if __name__ == '__main__':
    unittest.main()
