#!/usr/bin/python3
"""This is used to define a HBNB console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def tokenizer(arguments):
    braces = re.search(r"\{(.*?)\}", arguments)
    bracket = re.search(r"\[(.*?)\]", arguments)
    if braces is None:
        if bracket is None:
            return[i.strip(",") for i in split(arguments)]
        else:
            lexical_analizer = split(arguments[:bracket.span()[0]])
            return_list = [i.strip(",") for i in lexical_analizer]
            return_list.append(bracket.group())
            return return_list
    else:
        lexical_analizer = split(arguments[:braces.span()[0]])
        return_list = [i.strip(",") for i in lexical_analizer]
        return_list.append(braces.group())
        return return_list
    
    
class HBNBCommand(cmd.Cmd):
    """This defines the HolbertonBnB command interpreter
    
    Attributes:
        prompt: This is the command prompt.
    """
    
    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review",
    }
    
    def blank_line(self):
        """This does not do anything upon receiving a blank line"""
        pass
    
    def levant(self, arguments):
        """This is the behaviour of the cmd when input is invalid"""
        argument_dictionary = {
            "all": self.all,
            "show": self.show,
            "destroy": self.destroy,
            "count": self.count,
            "update": self.update   
        }
        compare = re.search(r"\.", arguments)
        if compare is not None:
            argument_1 = [arguments[:compare.span()[0]], arguments[compare.span():]]
            compare = re.search(r"\((.*?)\)", argument_1[1])
            if compare is not None:
                comms = [argument_1[1][:compare.span()[0]], compare.group()[1:-1]]
                if comms[0] in argument_dictionary.keys():
                    shout = "{} {}".format(argument_1[0], comms[1])
                    return argument_dictionary[comms[0]](shout)
        print("*** Syntax not Known: {}".format(arguments))
        return False
    
    def quitter(self, arguments):
        """This is used to quit the program"""
        return True
    
    def EOF(self, arguments):
        """This is used to signify The Eof"""
        print("")
        return True
    
    def create(self, arguments):
        """Usage: This creates <class>
        This creates a new class instance and prints its instance
        """
        argument_1 = tokenizer(arguments)
        if len(argument_1) == 0:
            print("** class name missing **")
        elif argument_1[0] not in HBNBCommand.__classes:
            print("** class doesnt exist **")
        else:
            print(eval(argument_1[0])().id)
            storage.save
            
    def show(self, arguments):
        """Usage: This shows <class> <id> or <class.show(<id>)
        This is used to display a string representation of a class instance
        """
        argument_1 = tokenizer(arguments)
        object_dictionary = storage.all()
        if len(argument_1) == 0:
            print("** class name missing **")
        elif argument_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument_1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument_1[0], argument_1[1]) not in object_dictionary:
            print("** no instance found **")
        else:
            print(object_dictionary["{}.{}".format(argument_1[0], argument_1[1])])
            
    def destroy(self, arguments):
        """Usage: This is used to destroy <class> <id> or <class>.destroy(<id>)
        This deletes a class instance of a given id"""
        argument_1 = tokenizer(arguments)
        object_dictionary = storage.all()
        if len(argument_1) == 0:
            print("** class name missing **")
        elif argument_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument_1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument_1[0], argument_1[1]) not in object_dictionary.keys():
            print("** no instance found **")
        else:
            del object_dictionary["{}.{}".format(argument_1[0], argument_1[1])]
            storage.save()
            
    def all(self, arguments):
        """Usage: all or all <class> or whatever
        This displays string representations of all instances of a class
        if no class is specified, it just displays all objjects"""
        argument_1 = tokenizer(arguments)
        if len(argument_1) > 0 and argument_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            object_1 = []
            for object in storage.all().values():
                if len(argument_1) > 0 and argument_1[0] == object.__class__.__name__:
                    object_1.append(object.__str__())
                elif len(argument_1) == 0:
                    object_1.append(object.__str__())
            print(object_1)
            
    def count(self, argument):
        """Usage: count
        This retrieves the number of instances of a given class"""
        argument_1 = tokenizer(argument)
        counter = 0
        for object in storage.all().values():
            if argument_1[0] == object.__class__.__name__:
                counter = counter + 1
        print(counter)
        
    def update(self, arguments):
        """This is used to update a class attribute of a given id"""
        argument_1 = tokenizer(arguments)
        object_dictionary = storage.all()
        
        if len(argument_1) == 0:
            print("** class name missing **")
            return False
        if argument_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argument_1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argument_1[0], argument_1[1]) not in object_dictionary.keys():
            print("** attribute name missing **")
            return False
        if len(argument_1) == 2:
            print("** attribute name missing **")
            return False
        if len(argument_1) == 3:
            try:
                type(eval(argument_1[2])) != dict
            except NameError:
                print("** value missing **")
                return False
            
        if len(argument_1) == 4:
            object = object_dictionary["{}.{}".format(argument_1[0], argument_1[1])]
            if argument_1[2] in object.__class__.__dict__.keys():
                value_type = type(object.__class__.__dict__[argument_1[2]])
                object.__dict__[argument_1[2]] == value_type(argument_1[3])
            else:
                object.__dict__[argument_1[2]] = value_type(argument_1[3])
        elif type(eval(argument_1[2])) == dict:
            object = object_dictionary["{}.{}".format(argument_1[0], argument_1[1])]
            for i, j in eval(argument_1[2].items()):
                if (i in object.__class__.__dict__.keys() and
                        type(object.__class__.__dict__[i]) in {str, int, float}):
                    value_type = type(object.__class__.__dict__[i])
                    object.__dict__[i] = value_type(j)
                else:
                    object.__dict__[i] = j
        storage.save()
        
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()        
            
            
    
        