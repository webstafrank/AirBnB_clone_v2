#!/usr/bin/python3
import re
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    # existing code...

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes()[class_name]()
        for param in args[1:]:
            match = re.match(r"(\w+)=(.+)", param)
            if match:
                key, value = match.groups()
                value = self.parse_value(value)
                if value is not None:
                    setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def parse_value(self, value):
        # Parse a string
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace('_', ' ').replace('\\"', '"')
            return value
        # Parse a float
        try:
            if '.' in value:
                return float(value)
        except ValueError:
            pass
        # Parse an integer
        try:
            return int(value)
        except ValueError:
            pass
        return None
