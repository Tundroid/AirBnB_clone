import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import shutil

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.model = FileStorage()
        if os.path.exists("file.json"):
            shutil.move("file.json", "file.json.backup")

    def test_init(self):
        self.assertTrue(hasattr(self.model, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.model, '_FileStorage__objects'))
        self.assertIsInstance(self.model._FileStorage__file_path, str)
        self.assertIsInstance(self.model._FileStorage__objects, dict)
        self.assertEqual(self.model._FileStorage__file_path, "file.json")
        self.assertEqual(self.model._FileStorage__objects, {})

    def test_all(self):
        self.assertEqual(self.model.all(), {})
        base_model = BaseModel()
        self.model.new(base_model)
        self.assertIn(base_model, self.model.all().values())

    def test_new(self):
        base_model = BaseModel()
        self.model.new(base_model)
        self.assertIn(base_model, self.model.all().values())

    def test_save(self):
        base_model = BaseModel()
        self.model.new(base_model)
        self.model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        base_model = BaseModel()
        self.assertEqual(len(self.model.all()), 0)
        self.model.new(base_model)
        self.assertEqual(len(self.model.all()), 1)
        self.model.save()
        self.model._FileStorage__objects = {}
        self.assertEqual(len(self.model.all()), 0)
        self.model.reload()
        self.assertEqual(len(self.model.all()), 1)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            self.model.reload(None)

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("file.json.backup"):
            shutil.move("file.json.backup", "file.json")

if __name__ == '__main__':
    unittest.main()
