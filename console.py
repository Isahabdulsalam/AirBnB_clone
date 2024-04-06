#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

    def do_help(self, line):
        """Show help message"""
        super().do_help(line)

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            instance = storage.get_object_by_id(class_name, instance_id)
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            instance = storage.get_object_by_id(class_name, instance_id)
            if instance:
                storage.delete_object(instance)
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances
        Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.        
        If no class is specified, displays all instantiated objects."""        
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
                    print(objl)
    def do_update(self, arg):
        """Update an instance based on class name and id (BaseModel or User)"""
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
            if len(args) == 4:
                obj = objdict["{}.{}".format(args[0], args[1])]
                if args[2] in obj.__class__.__dict__.keys():
                    valtype = type(obj.__class__.__dict__[args[2]])
                    obj.__dict__[args[2]] = valtype(args[3])
                else:
                    obj.__dict__[args[2]] = args[3]
            elif type(eval(args[2])) == dict:
                    obj = objdict["{}.{}".format(args[0], args[1])]
                    for a, b in eval(args[2]).items():
                        if (a in obj.__class__.__dict__.keys() and
                            type(obj.__class__.__dict__[a]) in {str, int, float}):
                            valtype = type(obj.__class__.__dict__[a])
                            obj.__dict__[a] = valtype(b)
            else:
                obj.__dict__[a] = b
                storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = eval(arg).__name__
            if class_name == "User":
                class_name = "models.user.User"
            count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == class_name)
            print(count)
        except NameError:
            print("** class doesn't exist **")

      
if __name__ == '__main__':
    HBNBCommand().cmdloop()
