import sys

sys.path.append("..")
import apache_beam as beam
from init_objects import InitObject
from utils.utils import get_logger, log

logger = get_logger(name=__name__)
class_objects = InitObject(class_config_path="./config/class_object.yaml")


class PreProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()

    @log(logger)
    def process(self, source: str):
        """ """
        PRP = class_objects.extract[source]
        results = PRP.extract()
        wrapper = {"source": source, "data": results}
        return [wrapper]


class InferenceProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()

    @log(logger)
    def process(self, element: dict):
        """ """
        source, data = element["source"], element["data"]
        IP = class_objects.transform[source]
        results = IP.transform(data)
        wrapper = {"source": source, "data": results}
        return [wrapper]


class PostProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()

    @log(logger)
    def process(self, element: dict):
        """ """
        source, data = element["source"], element["data"]
        POP = class_objects.load[source]
        POP.load(data)
        logger.info(f"ETL JOB: [{source}] SUCCESS!!")
