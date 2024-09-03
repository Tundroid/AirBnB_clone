import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage

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
            self.assertIn(f"User.{f.getvalue()}".strip("\n"), storage.all().keys())

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
#             self.assertEqual(expect, f.getvalue().strip("\n"))

#     def test_create_nonexistent_class(self):
#         with patch('sys.stdout', new=StringIO()) as f:
#             expect = "** class doesn't exist **"
#             HBNBCommand().onecmd("create NoModel")
#             self.assertEqual(expect, f.getvalue().strip("\n"))

#     def test_create_existing_class(self):
#         with patch('sys.stdout', new=StringIO()) as f:
#             HBNBCommand().onecmd("create User")
#             self.assertIn(f"User.{f.getvalue()}".strip("\n"), storage.all().keys())

class TestHBNBCommandShow(unittest.TestCase):

    def test_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** class name missing **"
            HBNBCommand().onecmd("show")
            self.assertEqual(expect, f.getvalue().strip("\n"))

    def test_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** class doesn't exist **"
            HBNBCommand().onecmd("show NoModel")
            self.assertEqual(expect, f.getvalue().strip("\n"))

    def test_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** instance id missing **"
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(expect, f.getvalue().strip("\n"))

    def test_nonexistent_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** no instance found **"
            HBNBCommand().onecmd("show BaseModel no_id12340")
            self.assertEqual(expect, f.getvalue().strip("\n"))

class TestHBNBCommandDestroy(unittest.TestCase):

    def test_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            expect = "** class name missing **"
            HBNBCommand().onecmd("destroy")
            self.assertEqual(expect, f.getvalue().strip("\n"))

    # def test_nonexistent_class(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** class doesn't exist **"
    #         HBNBCommand().onecmd("show NoModel")
    #         self.assertEqual(expect, f.getvalue().strip("\n"))

    # def test_missing_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** instance id missing **"
    #         HBNBCommand().onecmd("show BaseModel")
    #         self.assertEqual(expect, f.getvalue().strip("\n"))

    # def test_nonexistent_id(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         expect = "** no instance found **"
    #         HBNBCommand().onecmd("show BaseModel no_id12340")
    #         self.assertEqual(expect, f.getvalue().strip("\n"))

if __name__ == '__main__':
    unittest.main()
