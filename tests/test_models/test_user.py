import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.model = User()

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
        kwargs = {
            'id': 'e49ada22-140b-4f58-8a1d-6af38c5dda19',
            'created_at': '2024-09-03T12:00:00',
            'updated_at': '2024-09-03T12:00:00',
            'email': 'test@mail.com',
            'password': 'my_password',
            'first_name': 'John',
            'last_name': 'Smith'
        }
        model = User(**kwargs)
        self.assertEqual(model.email, 'test@mail.com')
        self.assertEqual(model.password, 'my_password')
        self.assertEqual(model.first_name, 'John')
        self.assertEqual(model.last_name, 'Smith')

    def test_to_dict(self):
        self.model.email = "test@mail.com"
        self.model.password = "my_password"
        self.model.first_name = "John"
        self.model.last_name = "Smith"
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['email'], self.model.email)
        self.assertEqual(model_dict['password'], self.model.password)
        self.assertEqual(model_dict['first_name'], self.model.first_name)
        self.assertEqual(model_dict['last_name'], self.model.last_name)


if __name__ == '__main__':
    unittest.main()
