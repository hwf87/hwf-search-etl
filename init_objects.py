
import yaml
import json
from utils.utils import log, get_logger

logger = get_logger(name=__name__)

class InitObject():
    def __init__(self, class_object_path: str) -> None:
        self.class_config = self._load_from_config(path = class_object_path)
        # self.extract = self._implement(key = "extract")
        # self.transform = self._implement(key = "transform")
        # self.load = self._implement(key = "load")

    def _load_from_config(self, path: str):
        """
        """
        with open(path, "r") as f:
            class_config = yaml.load(f, Loader=yaml.FullLoader)
        return class_config

    def _implement(self, key):
        """
        """
        pass

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



    def _instance_class(self):
        """
        """
        pass

    def _load_class(self):
        """
        """
        pass

if __name__ == "__main__":
    class_object = InitObject(class_object_path = "./config/class_object.yaml")
    print(class_object.class_config["extract"])
    class_object._process_class(class_object.class_config["extract"])
