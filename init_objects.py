# -*- coding: utf-8 -*-

import yaml
import importlib
from utils.utils import log, get_logger

logger = get_logger(name=__name__)


class InitObject:
    def __init__(self, class_config_path: str) -> None:
        self.class_config = self._read_config(path=class_config_path)
        self.extract = self._create(key="extract")
        self.transform = self._create(key="transform")
        self.load = self._create(key="load")

    @log(logger)
    def _read_config(self, path: str) -> dict:
        """ """
        with open(path, "r") as f:
            class_config = yaml.load(f, Loader=yaml.FullLoader)
        return class_config

    @log(logger)
    def _load_class(self, class_config_dict: dict) -> dict:
        """ """
        class_object_dict = {}
        for key, val in class_config_dict.items():
            for key2, val2 in val.items():
                class_object_dict[key2] = getattr(importlib.import_module(key), val2)
        return class_object_dict

    @log(logger)
    def _instance_class(self, class_object_dict: dict) -> dict:
        """ """
        instance_calss_dict = {}
        for key, val in class_object_dict.items():
            instance_calss_dict[key] = val()
        return instance_calss_dict

    @log(logger)
    def _create(self, key) -> dict:
        """ """
        class_config_dict = self.class_config[key]
        class_object_dict = self._load_class(class_config_dict=class_config_dict)
        instance_calss_dict = self._instance_class(class_object_dict=class_object_dict)
        return instance_calss_dict
