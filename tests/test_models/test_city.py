import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.model = City()
        self.kwargs = {
            'id': 'e49ada22-140b-4f58-8a1d-6af38c5dda19',
            'created_at': '2024-09-03T12:00:00',
            'updated_at': '2024-09-03T12:00:00',
            'state_id': 'cd609fa0-7191-4508-ab38-54487b953e66',
            'name': 'Manassas'
        }

    def test_init_without_kwargs(self):
        self.assertTrue(hasattr(self.model, 'state_id'))
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertIsInstance(self.model.state_id, str)
        self.assertIsInstance(self.model.name, str)

    def test_init_with_kwargs(self):
        model = City(**self.kwargs)
        self.assertEqual(model.state_id, self.kwargs['state_id'])
        self.assertEqual(model.name, self.kwargs['name'])

    def test_to_dict(self):
        model_dict = City(**self.kwargs).to_dict()
        self.assertEqual(model_dict['state_id'], self.kwargs['state_id'])
        self.assertEqual(model_dict['name'], self.kwargs['name'])

if __name__ == '__main__':
    unittest.main()
