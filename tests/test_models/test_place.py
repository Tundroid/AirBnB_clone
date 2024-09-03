import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.model = Place()
        self.kwargs = {
            'id': 'e49ada22-140b-4f58-8a1d-6af38c5dda19',
            'created_at': '2024-09-03T12:00:00',
            'updated_at': '2024-09-03T12:00:00',
            'city_id': 'cd609fa0-7191-4508-ab38-54487b953e66',
            'user_id': 'cd609fa0-7191-4508-ab38-54487b953e67',
            'name': 'Oregon DR',
            'description': 'Noice',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 300,
            'latitude': 5432.1,
            'longitude': 1234.5,
            'amenity_ids': ['cd609fa0-7191-4508-ab38-54487b953e68',
                            'cd609fa0-7191-4508-ab38-54487b953e69']
        }

    def test_init_without_kwargs(self):
        self.assertTrue(hasattr(self.model, 'city_id'))
        self.assertTrue(hasattr(self.model, 'user_id'))
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertTrue(hasattr(self.model, 'description'))
        self.assertTrue(hasattr(self.model, 'number_rooms'))
        self.assertTrue(hasattr(self.model, 'number_bathrooms'))
        self.assertTrue(hasattr(self.model, 'max_guest'))
        self.assertTrue(hasattr(self.model, 'price_by_night'))
        self.assertTrue(hasattr(self.model, 'latitude'))
        self.assertTrue(hasattr(self.model, 'longitude'))
        self.assertTrue(hasattr(self.model, 'amenity_ids'))
        self.assertIsInstance(self.model.city_id, str)
        self.assertIsInstance(self.model.user_id, str)
        self.assertIsInstance(self.model.name, str)
        self.assertIsInstance(self.model.description, str)
        self.assertIsInstance(self.model.number_rooms, int)
        self.assertIsInstance(self.model.number_bathrooms, int)
        self.assertIsInstance(self.model.max_guest, int)
        self.assertIsInstance(self.model.price_by_night, int)
        self.assertIsInstance(self.model.latitude, float)
        self.assertIsInstance(self.model.longitude, float)
        self.assertIsInstance(self.model.amenity_ids, list)

    def test_init_with_kwargs(self):
        model = Place(**self.kwargs)
        self.assertEqual(model.city_id, self.kwargs['city_id'])
        self.assertEqual(model.user_id, self.kwargs['user_id'])
        self.assertEqual(model.name, self.kwargs['name'])
        self.assertEqual(model.description, self.kwargs['description'])
        self.assertEqual(model.number_rooms, self.kwargs['number_rooms'])
        self.assertEqual(model.number_bathrooms, self.kwargs['number_bathrooms'])
        self.assertEqual(model.max_guest, self.kwargs['max_guest'])
        self.assertEqual(model.price_by_night, self.kwargs['price_by_night'])
        self.assertEqual(model.latitude, self.kwargs['latitude'])
        self.assertEqual(model.longitude, self.kwargs['longitude'])
        self.assertEqual(model.amenity_ids, self.kwargs['amenity_ids'])

    def test_to_dict(self):
        model_dict = Place(**self.kwargs).to_dict()
        self.assertEqual(model_dict['city_id'], self.kwargs['city_id'])
        self.assertEqual(model_dict['user_id'], self.kwargs['user_id'])
        self.assertEqual(model_dict['name'], self.kwargs['name'])
        self.assertEqual(model_dict['description'], self.kwargs['description'])
        self.assertEqual(model_dict['number_rooms'], self.kwargs['number_rooms'])
        self.assertEqual(model_dict['number_bathrooms'], self.kwargs['number_bathrooms'])
        self.assertEqual(model_dict['max_guest'], self.kwargs['max_guest'])
        self.assertEqual(model_dict['price_by_night'], self.kwargs['price_by_night'])
        self.assertEqual(model_dict['latitude'], self.kwargs['latitude'])
        self.assertEqual(model_dict['longitude'], self.kwargs['longitude'])
        self.assertEqual(model_dict['amenity_ids'], self.kwargs['amenity_ids'])


if __name__ == '__main__':
    unittest.main()
