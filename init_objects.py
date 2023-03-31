# -*- coding: utf-8 -*-

import yaml
import json
import importlib
from utils.utils import log, get_logger

logger = get_logger(name=__name__)

class InitObject():
    def __init__(self, class_object_path: str) -> None:
        self.class_config = self._load_from_config(path = class_object_path)
        self.extract = self._implement(key = "extract")
        self.transform = self._implement(key = "transform")
        self.load = self._implement(key = "load")

    def _load_from_config(self, path: str):
        """
        """
        with open(path, "r") as f:
            class_config = yaml.load(f, Loader=yaml.FullLoader)
        return class_config

    def _process_class(self, content: json) -> dict:
        """
        """
        new_map = {}
        for key, val in content.items():
            class_name = []
            for key2, val2 in val.items():
                class_name.append((key2, val2))
            new_map[key] = class_name
        print(new_map)
        return new_map
    
    def _load_class(self, class_map: dict) -> dict:
        """
        """
        class_object_dict = {}
        for _, key in enumerate(class_map):
            content = class_map[key]
            for _, key2 in enumerate(content):
                class_object_dict[key2[0]] = getattr(importlib.import_module(key), key2[1])
        return class_object_dict

    def _instance_class(self, class_object_dict: dict) -> dict:
        """
        """
        instance_calss_dict = {}
        for _, key in enumerate(class_object_dict):
            instance_calss_dict[key] = class_object_dict[key]()
        return instance_calss_dict
    
    def _implement(self, key) -> dict:
        """
        """
        new_map = self._process_class(self.class_config[key])
        class_object_dict = self._load_class(class_map=new_map)
        instance_calss_dict = self._instance_class(class_object_dict=class_object_dict)
        return instance_calss_dict

   

if __name__ == "__main__":
    class_object = InitObject(class_object_path = "./config/class_object.yaml")
    print(class_object.extract)
    print("====================")

    print(class_object.transform)
    print("====================")

    print(class_object.load)

    # print(class_object.class_config["extract"])
    # new_map = class_object._process_class(class_object.class_config["extract"])
    # class_object_dict = class_object._load_class(class_map=new_map)
    # print(class_object_dict)
    # instance_calss_dict = class_object._instance_class(class_object_dict=class_object_dict)
    # print(instance_calss_dict["news"])
