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
            obj_list.append(str(obj))
        print(obj_list)

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
        if line.startswith("BaseModel.all()"):
            self.do_BaseModel_all(line[len("BaseModel.all()"):].strip())
        elif line.startswith("User.all()"):
            self.do_User_all(line[len("User.all()"):].strip())
        elif line.startswith("State.all()"):
            self.do_State_all(line[len("State.all()"):].strip())
        elif line.startswith("City.all()"):
            self.do_City_all(line[len("City.all()"):].strip())
        elif line.startswith("Place.all()"):
            self.do_Place_all(line[len("Place.all()"):].strip())
        elif line.startswith("Amenity.all()"):
            self.do_Amenity_all(line[len("Amenity.all()"):].strip())
        elif line.startswith("Review.all()"):
            self.do_Review_all(line[len("Review.all()"):].strip())
        else:
            print(f"Command not recognized: {line}")

    def get_obj_list(self, obj_class):
        obj_list = []
        for obj in storage.all().values():
            if type(obj) is obj_class:
                obj_list.append(str(obj))
        return obj_list

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

    def do_EOF(self, arg):
        exit()

    def do_quit(self, arg):
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
