#!/usr/bin/python3
"""Console Module"""

import cmd
import json
import re
import shlex

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class implementation inheriting from cmd.Cmd"""

    prompt = '(hbnb) '

    def syntax_check(self, args=[], id_check=True):
        """Check if a given class exists."""
        if args:
            try:
                globals()[args[0]]
                if id_check and len(args) == 1:
                    print("** instance id missing **")
                    return False
                return True
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return False

    def do_create(self, arg):
        """Create a new instance of a class."""
        args = shlex.split(arg)
        if self.syntax_check(args, False):
            new_obj = eval(args[0])()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Display the string representation of an instance."""
        args = shlex.split(arg)
        if self.syntax_check(args):
            try:
                obj = storage.all()[f"{args[0]}.{args[1]}"]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        if self.syntax_check(args):
            try:
                del storage.all()[f"{args[0]}.{args[1]}"]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """Display all instances or all instances of a specific class."""
        if arg:
            args = shlex.split(arg)
            if not self.syntax_check(args, False):
                return
        obj_list = []
        for obj in storage.all().values():
            if arg:
                if type(obj) is eval(args[0]):
                    obj_list.append(str(obj))
            else:
                obj_list.append(str(obj))
        print(obj_list)

    def do_count(self, arg):
        """Count the instances of a class."""
        if arg:
            args = shlex.split(arg)
            if not self.syntax_check(args, False):
                return
        count = 0
        for obj in storage.all().values():
            if arg:
                if type(obj) is eval(args[0]):
                    count += 1
            else:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update an instance attribute or create a new instance."""
        args = shlex.split(arg)
        if self.syntax_check(args):
            try:
                attribs = args[1:]
                obj = storage.all()[f"{args[0]}.{attribs[0]}"]
                if len(attribs) > 1:
                    if len(attribs) > 2:
                        setattr(obj, attribs[1], attribs[2])
                        storage.save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            except KeyError:
                print("** no instance found **")

    def default(self, line):
        """Handle unrecognized commands."""

        pattern_generic = re.compile(r'^.*\..*\(.*\)$')
        pattern_id = re.compile(r'^.*\..*\(\s*".*"\s*\)$')
        pattern_attr = re.compile(r'^.*\..*\(\s*".*"\s*,\s*".*"\s*,?.*?\)$')
        pattern_dict = re.compile(r'^.*\..*\(\s*".*"\s*,\s*\{.*\}\s*\)$')

        if pattern_generic.match(line):
            command = line.split(".")[1].split("(")[0]
            model = line.split(".")[0]
            if pattern_dict.match(line):
                pattern = re.compile(r'\(.*\)')
                args = pattern.search(line).group(0).strip("()").split(",")
                id = args[0].strip(' "')
                pattern = re.compile(r'\{.*\}')
                try:
                    dict = pattern.search(line).group(0).replace("'", '"')
                    dict = json.loads(dict)
                    for attr, val in dict.items():
                        val = f"'{val}'" if isinstance(val, str) else val
                        self.onecmd(f"{command} {model} {id} {attr} {val}")
                except json.decoder.JSONDecodeError:
                    print("** invalid dictionary **")
            elif pattern_attr.match(line):
                pattern = re.compile(r'\(.*\)')
                args = pattern.search(line).group(0).strip("()").split(",")
                id = args[0].strip('"')
                attr = args[1]
                val = "" if len(args) < 3 else args[2]
                self.onecmd(f"{command} {model} {id} {attr} {val}")
            elif pattern_id.match(line):
                pattern = re.compile(r'".*"')
                id = pattern.search(line).group(0).strip('"')
                self.onecmd(f"{command} {model} {id}")
            else:
                self.onecmd(f"{command} {model}")
        else:
            print(f"Command not recognized: {line}")

    def do_EOF(self, arg):
        """Exit the console on EOF."""
        return True

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
