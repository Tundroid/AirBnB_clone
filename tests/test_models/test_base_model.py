import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_init_without_kwargs(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_init_with_kwargs(self):
        kwargs = {
            'id': 'e49ada22-140b-4f58-8a1d-6af38c5dda19',
            'created_at': '2024-09-03T12:00:00',
            'updated_at': '2024-09-03T12:00:00'
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, 'e49ada22-140b-4f58-8a1d-6af38c5dda19')
        self.assertEqual(model.created_at, datetime.datetime.fromisoformat('2024-09-03T12:00:00'))
        self.assertEqual(model.updated_at, datetime.datetime.fromisoformat('2024-09-03T12:00:00'))

    def test_str_representation(self):
        self.assertEqual(str(self.model), f"[BaseModel] ({self.model.id}) {self.model.__dict__}")

    def test_save(self):
        updated_at = self.model.updated_at
        self.assertNotEqual(self.model.updated_at, updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
