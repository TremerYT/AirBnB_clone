#!/usr/bin/python3
"""This is the cmd"""
import cmd
import sys
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """This reps the cmd"""
    prompt = "(hbnb) "
    models = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    @staticmethod
    def tokenizer(input=None, deli=" "):
        """This is the tokenizer"""
        if input is not None:
            return input.split(deli)

    def do_quit(self, arg):
        """This is the quitter"""
        sys.exit()

    def do_EOF(self, arg):
        """This checks EOF"""
        sys.exit()

    def do_help(self, arg):
        """This i for help"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """This creates new instances"""
        argl = self.split_string(arg)
        if argl[0] == "":
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            arg = HBNBCommand.models[argl[0]]()
            print(arg.id)
            arg.save()

    def do_show(self, arg):
        """This prints all details"""
        if arg == "":
            print("** class name missing **")
            return
        try:
            args = self.split_string(arg, " ")
            if args[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
                return
            obj = f"{args[0]}.{args[1]}"
            keys = storage.all()
            for i in keys.keys():
                if i == obj:
                    print(keys[i])
                    return
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """This destroys aclaas"""
        if arg == "":
            print("** class name missing **")
            return
        try:
            args = self.split_string(arg, " ")
            if args[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
                return
            obj = f"{args[0]}.{args[1]}"
            keys = storage.all()
            del keys[obj]
            storage.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """This displays all instances"""
        keys = storage.all()
        keydict = []
        argl = self.split_string(arg)
        if argl[0] == "":
            keydict = [str(keys[i]) for i in keys.keys()]
        elif argl[0] in HBNBCommand.models:
            for i in keys.keys():
                if i.startswith(argl[0]):
                    keydict.append(str(keys[i]))
        else:
            print("** class doesn't exist **")
            return
        print(keydict)

    def do_update(self, arg):
        """This updates instances"""
        try:
            if arg == "":
                raise NameError
            args = self.split_string(arg)
            if args[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
                return
            elif len(args) == 1 or args[1] == "":
                print("** instance id missing **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            name = f"{args[0]}.{args[1]}"
            odict = {}
            for i in range(2, len(args), 2):
                key = args[i]
                key = key.replace("{", "").replace(":", "")
                key = key.replace("}", "").replace('"', "").replace("'", "")
                val = args[i + 1]
                val = val.replace("{", "").replace(":", "")
                val = val.replace("}", "").replace('"', "").replace("'", "")
                odict[key] = value
            keys = storage.all()
            if name in keys:
                obj = keys[name]
                for i, j in odict.items():
                    setattr(obj, i, j)
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print('** class name missing **')
        except IndexError:
            print("** value missing **")

    def do_count(self, arg):
        """This counts number of instances"""
        if arg == "":
            print("** class name missing **")
            return
        argl = self.split_string(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def emptyline(self):
        """Do nthing"""
        return

    def default(self, arg):
        """This is the default"""
        coms = {
            "create": self.do_create,
            "all": self.do_all,
            "count": self.do_count,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "show": self.do_show
        }
        args = re.match(r"(?P<model>\w+)\.(?P<act>\w+)\((?P<det>.*?)\)", arg)
        if args:
            model = args.group("model")
            act = args.group("act")
            det = args.group("det")
            det = det.replace(",", "")
            coms[act](f"{model} {det}")
        else:
            print(f"** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
