#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import shlex
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def safety_check(self, arg=None):
        if arg:
            try:
                tokens = self.parseline(arg)
                eval(tokens[0]).__class__
                return True
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return False

    def do_create(self, arg):
        if self.safety_check(arg):
            new_obj = eval(arg)()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)

    def do_show(self, arg):
        if self.safety_check(arg):
            tokens = self.parseline(arg)
            if len(tokens[1]) == 0:
                print("** instance id missing **")
                return
            try:
                obj = storage.all()[f"{tokens[0]}.{tokens[1]}"]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        if self.safety_check(arg):
            tokens = self.parseline(arg)
            if len(tokens[1]) == 0:
                print("** instance id missing **")
                return
            try:
                del storage.all()[f"{tokens[0]}.{tokens[1]}"]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        if arg:
            if not self.safety_check(arg):
                return
        obj_list = []
        for obj in storage.all().values():
            if arg:
                if type(obj) is eval(arg):
                    obj_list.append(str(obj))
            else:
                obj_list.append(str(obj))
        print(obj_list)

    def do_count(self, arg):
        if arg:
            if not self.safety_check(arg):
                return
        count = 0
        for obj in storage.all().values():
            if arg:
                if type(obj) is eval(arg):
                    count += 1
            else:
                count += 1
        print(count)

    def do_update(self, arg):
        if self.safety_check(arg):
            tokens = self.parseline(arg)
            if len(tokens[1]) == 0:
                print("** instance id missing **")
                return
            try:
                attribs = shlex.split(tokens[1])
                obj = storage.all()[f"{tokens[0]}.{attribs[0]}"]
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

        pattern_with_id = re.compile(r'^.*\..*\(".*"\)$')
        pattern_generic = re.compile(r'^.*\..*\(\)$')

        if pattern_generic.match(line):
            command = line.split(".")[1].split("(")[0]
            model = line.split(".")[0]
            self.onecmd(f"{command} {model}")
        elif pattern_with_id.match(line):
            command = line.split(".")[1].split("(")[0]
            model = line.split(".")[0]
            pattern = re.compile(r'".*"')
            id = pattern.search(line).group(0).strip('"')
            self.onecmd(f"{command} {model} {id}")
        else:
            print(f"Command not recognized: {line}")

    def get_obj_list(self, obj_class):
        obj_list = []
        for obj in storage.all().values():
            if type(obj) is obj_class:
                obj_list.append(str(obj))
        return obj_list

    def get_obj_count(self, obj_class):
        count = 0
        for obj in storage.all().values():
            if type(obj) is obj_class:
                count += 1
        return count

    def do_BaseModel_all(self, arg):
        print(self.get_obj_list(BaseModel))

    def do_User_all(self, arg):
        print(self.get_obj_list(User))

    def do_State_all(self, arg):
        print(self.get_obj_list(State))

    def do_City_all(self, arg):
        print(self.get_obj_list(City))

    def do_Place_all(self, arg):
        print(self.get_obj_list(Place))

    def do_Amenity_all(self, arg):
        print(self.get_obj_list(Amenity))

    def do_Review_all(self, arg):
        print(self.get_obj_list(Review))

    def do_BaseModel_count(self, arg):
        print(self.get_obj_count(BaseModel))

    def do_User_count(self, arg):
        print(self.get_obj_count(User))

    def do_State_count(self, arg):
        print(self.get_obj_count(State))

    def do_City_count(self, arg):
        print(self.get_obj_count(City))

    def do_Place_count(self, arg):
        print(self.get_obj_count(Place))

    def do_Amenity_count(self, arg):
        print(self.get_obj_count(Amenity))

    def do_Review_count(self, arg):
        print(self.get_obj_count(Review))

    def do_EOF(self, arg):
        exit()

    def do_quit(self, arg):
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
