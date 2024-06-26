#!/usr/bin/python3
# Models/engine/file_storage.py

class FileStorage:
    import json
from os import path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    objects_dict = json.load(file)
                    for key, value in objects_dict.items():
                        class_name, obj_id = key.split('.')
                        # Import class dynamically
                        from models import __dict__ as models_dict
                        class_obj = models_dict[class_name]
                        # Create instance from dictionary
                        obj_instance = class_obj(**value)
                        self.__objects[key] = obj_instance
                except Exception:
                    pass

    def delete(self, obj=None):
        """Delete obj from __objects if it exists."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

