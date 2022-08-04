#!/usr/bin/env python3
"""Console module for Airbnb clone"""

import cmd
import json
import models
from models.base_model import BaseModel
import gc


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
        Show all instances of a class
        Usage: "all" OR "all <class_name>"

        It can also be used to show all instances based on class name
        Example: all OR all BaseModel
        """

        args = parse(arg)
        if len(args) < 1:
            # print(json.dumps(getInstances()))
            print("All instances")
            return False
        if args[0] in classes:
            all_obj = models.storage.all()
            return_list = []
            for key, value in all_obj.items():
                if type(value).__name__ == args[0]:
                    return_list.append(str(value))
            print(return_list)
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
            all_obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in all_obj:
                print("** no instance found **")
                return False
            print(all_obj[key])
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
            new_obj = eval("{}()".format(args[0]))
            new_obj.save()
            print(new_obj.id)

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
            all_obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_obj:
                del all_obj[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        """Define behaviour when an empty line is entered"""
        pass

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the
        JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = parse(arg)
        length_of_args = len(args)
        if length_of_args < 1:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif length_of_args < 2:
            print("** instance id missing **")
        else:
            all_obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in all_obj:
                print("** no instance found **")
                return False
            my_obj = all_obj[key]
        if length_of_args < 3:
            print("** attribute name missing **")
        elif length_of_args < 4:
            print("** value missing **")
        else:
            my_obj.__dict__[args[2]] = args[3].strip('\"')
            my_obj.save()


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
