import apache_beam as beam
# from apache_beam.options.pipeline_options import PipelineOptions

import sys
sys.path.append("..")
from src.ProcessorBase import PreProcessor, InferenceProcessor, PostProcessor

def run():
   """
   """
   pre_processor = PreProcessor()
   inference_processor = InferenceProcessor()
   post_processor = PostProcessor()
   with beam.Pipeline() as pipeline:
      (
         pipeline
         | "Trigger" >> beam.Create(["houzz"]) #["news", "tedtalk"]
         | "Pre-Process" >> beam.ParDo(pre_processor)
         | "Inference" >> beam.ParDo(inference_processor)
         | "Post-Process" >> beam.ParDo(post_processor)
      )

if __name__ == '__main__': 
   run()