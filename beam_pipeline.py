import sys
sys.path.append("..")
import apache_beam as beam
from utils.utils import log, get_logger
from src.ProcessorBase import PreProcessor, InferenceProcessor, PostProcessor

logger = get_logger(name=__name__)

@log(logger)
def run():
   """
   """
   data_source = sys.argv[1]
   logger.info(f"Data Source: {data_source}")
   pre_processor = PreProcessor()
   inference_processor = InferenceProcessor()
   post_processor = PostProcessor()
   with beam.Pipeline() as pipeline:
      (
         pipeline
         | "Trigger" >> beam.Create([data_source]) #["houzz", "news", "tedtalk"]
         | "Pre-Process" >> beam.ParDo(pre_processor)
         | "Inference" >> beam.ParDo(inference_processor)
         | "Post-Process" >> beam.ParDo(post_processor)
      )

if __name__ == '__main__': 
   run()