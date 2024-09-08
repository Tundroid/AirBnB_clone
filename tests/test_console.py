import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
import models
from models.engine.file_storage import FileStorage
import os
import shutil



class TestHBNBCommand(unittest.TestCase):

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", f.getvalue())

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIn("Exit the console.", f.getvalue())

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertIn(f"User.{f.getvalue()}".strip(), storage.all().keys())

    # def test_show(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("create User")
    #         user_id = f.getvalue().strip()
    #         HBNBCommand().onecmd(f"show User {user_id}")
    #         self.assertIn(user_id, f.getvalue())

    # def test_destroy(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("create User")
    #         user_id = f.getvalue().strip()
    #         HBNBCommand().onecmd(f"destroy User {user_id}")
    #         self.assertNotIn(user_id, f.getvalue())

    # def test_all(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("create User")
    #         HBNBCommand().onecmd("all")
    #         self.assertIn("User", f.getvalue())

    # def test_count(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("create User")
    #         HBNBCommand().onecmd("count")
    #         self.assertIn("1", f.getvalue())

    # def test_update(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("create User")
    #         user_id = f.getvalue().strip()
    #         HBNBCommand().onecmd(f"update User {user_id} name John")
    #         self.assertIn("John", f.getvalue())
    
# class TestHBNBCommandCreate(unittest.TestCase):

#     def test_create(self):
#         with patch('sys.stdout', new=StringIO()) as f:
#             expect = "** class name missing **"
#             HBNBCommand().onecmd("create")
#             self.assertEqual(expect, f.getvalue().strip())

#     def test_create_nonexistent_class(self):
#         with patch('sys.stdout', new=StringIO()) as f:
#             expect = "** class doesn't exist **"
#             HBNBCommand().onecmd("create NoModel")
#             self.assertEqual(expect, f.getvalue().strip())

#     def test_create_existing_class(self):
#         with patch('sys.stdout', new=StringIO()) as f:
#             HBNBCommand().onecmd("create User")
#             self.assertIn(f"User.{f.getvalue()}".strip(), storage.all().keys())

class TestHBNBCommandShow(unittest.TestCase):

    def test_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** class name missing **"
            HBNBCommand().onecmd("show")
            self.assertEqual(expect, f.getvalue().strip())

    def test_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** class doesn't exist **"
            HBNBCommand().onecmd("show NoModel")
            self.assertEqual(expect, f.getvalue().strip())

    def test_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(expect, f.getvalue().strip())

    def test_nonexistent_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** no instance found **"
            HBNBCommand().onecmd("show BaseModel no_id12340")
            self.assertEqual(expect, f.getvalue().strip())

    def test_base_model_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_user_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("User.show()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_state_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("State.show()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_city_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("City.show()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_place_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Place.show()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_review_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Review.show()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_amenity_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Amenity.show()")
            self.assertEqual(expect, f.getvalue().strip())

class TestHBNBCommandDestroy(unittest.TestCase):

    def test_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** class name missing **"
            HBNBCommand().onecmd("destroy")
            self.assertEqual(expect, f.getvalue().strip())

    def test_base_model_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("BaseModel.destroy()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_user_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("User.destroy()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_state_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("State.destroy()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_city_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("City.destroy()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_place_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Place.destroy()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_review_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Review.destroy()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_amenity_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Amenity.destroy()")
            self.assertEqual(expect, f.getvalue().strip())

    # def test_nonexistent_class(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** class doesn't exist **"
    #         HBNBCommand().onecmd("show NoModel")
    #         self.assertEqual(expect, f.getvalue().strip())

    # def test_missing_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** instance id missing **"
    #         HBNBCommand().onecmd("show BaseModel")
    #         self.assertEqual(expect, f.getvalue().strip())

    # def test_nonexistent_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** no instance found **"
    #         HBNBCommand().onecmd("show BaseModel no_id12340")
    #         self.assertEqual(expect, f.getvalue().strip())

class TestHBNBCommandAll(unittest.TestCase):
    
    def setUp(self):
        if os.path.exists("file.json"):
            shutil.move("file.json", "file.json.backup")
        storage._FileStorage__objects = {}
    
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("file.json.backup"):
            shutil.move("file.json.backup", "file.json")

    def test_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "[]"
            HBNBCommand().onecmd("all")
            self.assertEqual(expect, f.getvalue().strip())

    def test_base_model_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "[]"
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_user_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "[]"
            HBNBCommand().onecmd("User.all()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_state_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "[]"
            HBNBCommand().onecmd("State.all()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_city_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "[]"
            HBNBCommand().onecmd("City.all()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_place_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "[]"
            HBNBCommand().onecmd("Place.all()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_review_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "[]"
            HBNBCommand().onecmd("Review.all()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_amenity_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "[]"
            HBNBCommand().onecmd("Amenity.all()")
            self.assertEqual(expect, f.getvalue().strip())

    # def test_nonexistent_class(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** class doesn't exist **"
    #         HBNBCommand().onecmd("show NoModel")
    #         self.assertEqual(expect, f.getvalue().strip())

    # def test_missing_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** instance id missing **"
    #         HBNBCommand().onecmd("show BaseModel")
    #         self.assertEqual(expect, f.getvalue().strip())

    # def test_nonexistent_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** no instance found **"
    #         HBNBCommand().onecmd("show BaseModel no_id12340")
    #         self.assertEqual(expect, f.getvalue().strip())

class TestHBNBCommandUpdate(unittest.TestCase):

    def test_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** class name missing **"
            HBNBCommand().onecmd("update")
            self.assertEqual(expect, f.getvalue().strip())

    def test_base_model_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("BaseModel.update()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_user_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("User.update()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_state_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("State.update()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_city_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("City.update()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_place_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Place.update()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_review_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Review.update()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_amenity_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("Amenity.update()")
            self.assertEqual(expect, f.getvalue().strip())

    # def test_nonexistent_class(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** class doesn't exist **"
    #         HBNBCommand().onecmd("show NoModel")
    #         self.assertEqual(expect, f.getvalue().strip())

    # def test_missing_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** instance id missing **"
    #         HBNBCommand().onecmd("show BaseModel")
    #         self.assertEqual(expect, f.getvalue().strip())

    # def test_nonexistent_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** no instance found **"
    #         HBNBCommand().onecmd("show BaseModel no_id12340")
    #         self.assertEqual(expect, f.getvalue().strip())

class TestHBNBCommandCount(unittest.TestCase):
    
    def setUp(self):
        if os.path.exists("file.json"):
            shutil.move("file.json", "file.json.backup")
        storage._FileStorage__objects = {}
    
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("file.json.backup"):
            shutil.move("file.json.backup", "file.json")

    def test_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "0"
            HBNBCommand().onecmd("count")
            self.assertEqual(expect, f.getvalue().strip())

    def test_base_model_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "0"
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_user_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "0"
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_state_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "0"
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_city_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "0"
            HBNBCommand().onecmd("City.count()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_place_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "0"
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_review_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "0"
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual(expect, f.getvalue().strip())

    def test_amenity_with_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "0"
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(expect, f.getvalue().strip())

    # def test_nonexistent_class(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** class doesn't exist **"
    #         HBNBCommand().onecmd("show NoModel")
    #         self.assertEqual(expect, f.getvalue().strip())

    # def test_missing_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** instance id missing **"
    #         HBNBCommand().onecmd("show BaseModel")
    #         self.assertEqual(expect, f.getvalue().strip())

    # def test_nonexistent_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** no instance found **"
    #         HBNBCommand().onecmd("show BaseModel no_id12340")
    #         self.assertEqual(expect, f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
