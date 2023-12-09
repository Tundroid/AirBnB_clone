#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


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

    def do_EOF(self, arg):
        exit()

    def do_quit(self, arg):
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
