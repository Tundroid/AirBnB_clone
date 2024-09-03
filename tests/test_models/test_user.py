import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.model = User()
        self.kwargs = {
            'id': 'e49ada22-140b-4f58-8a1d-6af38c5dda19',
            'created_at': '2024-09-03T12:00:00',
            'updated_at': '2024-09-03T12:00:00',
            'email': 'test@mail.com',
            'password': 'my_password',
            'first_name': 'John',
            'last_name': 'Smith'
        }

    def test_init_without_kwargs(self):
        self.assertTrue(hasattr(self.model, 'email'))
        self.assertTrue(hasattr(self.model, 'password'))
        self.assertTrue(hasattr(self.model, 'first_name'))
        self.assertTrue(hasattr(self.model, 'last_name'))
        self.assertIsInstance(self.model.email, str)
        self.assertIsInstance(self.model.password, str)
        self.assertIsInstance(self.model.first_name, str)
        self.assertIsInstance(self.model.last_name, str)

    def test_init_with_kwargs(self):
        model = User(**self.kwargs)
        self.assertEqual(model.email, self.kwargs['email'])
        self.assertEqual(model.password, self.kwargs['password'])
        self.assertEqual(model.first_name, self.kwargs['first_name'])
        self.assertEqual(model.last_name, self.kwargs['last_name'])

    def test_to_dict(self):
        model_dict = User(**self.kwargs).to_dict()
        self.assertEqual(model_dict['email'], self.kwargs['email'])
        self.assertEqual(model_dict['password'], self.kwargs['password'])
        self.assertEqual(model_dict['first_name'], self.kwargs['first_name'])
        self.assertEqual(model_dict['last_name'], self.kwargs['last_name'])


if __name__ == '__main__':
    unittest.main()
