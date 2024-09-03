import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.model = Review()
        self.kwargs = {
            'id': 'e49ada22-140b-4f58-8a1d-6af38c5dda19',
            'created_at': '2024-09-03T12:00:00',
            'updated_at': '2024-09-03T12:00:00',
            'place_id': 'cd609fa0-7191-4508-ab38-54487b953e66',
            'user_id': 'cd609fa0-7191-4508-ab38-54487b953e67',
            'text': "Very noice!"
        }

    def test_init_without_kwargs(self):
        self.assertTrue(hasattr(self.model, 'place_id'))
        self.assertTrue(hasattr(self.model, 'user_id'))
        self.assertTrue(hasattr(self.model, 'text'))
        self.assertIsInstance(self.model.place_id, str)
        self.assertIsInstance(self.model.user_id, str)
        self.assertIsInstance(self.model.text, str)

    def test_init_with_kwargs(self):
        model = Review(**self.kwargs)
        self.assertEqual(model.place_id, self.kwargs['place_id'])
        self.assertEqual(model.user_id, self.kwargs['user_id'])
        self.assertEqual(model.text, self.kwargs['text'])

    def test_to_dict(self):
        model_dict = Review(**self.kwargs).to_dict()
        self.assertEqual(model_dict['place_id'], self.kwargs['place_id'])
        self.assertEqual(model_dict['user_id'], self.kwargs['user_id'])
        self.assertEqual(model_dict['text'], self.kwargs['text'])

if __name__ == '__main__':
    unittest.main()
