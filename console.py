#!/usr/bin/env python3
"""Console module for Airbnb clone"""


import cmd
import json
# from . import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the command interpreter
        """
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter
        """
        print()
        return True

    def do_all(self, arg):
        """
        Show all instances
        Usage: all

        It can also be used to show all instances based on class name
        Usage: all className
        Example: all BaseModel
        """

        args = parse(arg)
        if len(args) < 1:
            # print(json.dumps(getInstances()))
            print("All instances")
            return False
        if args[0] in classes:
            # users = json.dumps(getinstances(args[0]))
            # print(users)
            print("All {} instances".format(args[0]))
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show all instances base on class name,
        Usage: show className
        Example: show BaseModel

        It can also be used to show a particular instance
        Usage: show className id
        Example: show User 1234-1234-1234
        """
        classes = ("BaseModel", "User")
        args = parse(arg)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) < 2:
                print("** instance id missing **")
                return False
            """all_obj = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in all_obj:
                print("** no instance found **")
                return False
            print(json.dumps(all_obj[key]))"""
            print("{}: {}".format(args[0], args[1]))
            return False
        else:
            print("** class doesn't exist **")

    def do_create(self, arg):
        """
        Create a new instance based on class name
        and return the id

        Usage: create className
        Example: create User
        """
        args = parse(arg)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            """new_obj = eval("{}()".format(args[0]))
            print(new_obj.id)"""
            print("test{}idtest{}id".format(args[0], args[0]))

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id

        Usage: destroy className id
        Example: destroy User 1234-1234-1234
        """
        args = parse(arg)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            """all_obj = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_obj:
                del all_obj[key]
            else:
                print("** no instance found **")"""

    def emptyline(self):
        """Define behaviour when an empty line is entered"""
        pass


classes = ("BaseModel", "User")


def parse(arg):
    """Convert input to a command and arguments"""

    return tuple(arg.split())

    """
    def getinstances(className=None):
        instanceList = []
        for obj in storage.all().values():
            if className is None:
                instanceList.append(obj)
            elif obj.__class__.__name__ == className:
                instanceList.append(obj)
        return instanceList
    """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
