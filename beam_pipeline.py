import apache_beam as beam

import sys
sys.path.append("..")
from src.ProcessorBase import PreProcessor, InferenceProcessor, PostProcessor

pre_processor = PreProcessor()
inference_processor = InferenceProcessor()
post_processor = PostProcessor()

# data = [[
#     {"id": 1, "text":"apple is a fruit!!"},
#     {"id": 2, "text":"sky is blue!!"},
#     {"id": 3, "text":"pencil is not a fruit!!"}
# ]]

def run():
   """
   """
   with beam.Pipeline() as pipeline:
      (
         pipeline
         | "Trigger" >> beam.Create(["Start Pipeline!"])
         | "Pre-Process" >> beam.ParDo(pre_processor)
         | "Inference" >> beam.ParDo(inference_processor)
         | "Post-Process" >> beam.ParDo(post_processor)
      )

run()