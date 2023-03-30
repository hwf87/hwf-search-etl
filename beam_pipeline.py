import apache_beam as beam
# from apache_beam.options.pipeline_options import PipelineOptions

import sys
sys.path.append("..")
from src.ProcessorBase import PreProcessor, InferenceProcessor, PostProcessor


from src.tedtalk.tedtalk_data_transformer import TedtalkTransformer
from src.tedtalk.tedtalk_data_extractor import TedtalkExtractor
from src.tedtalk.tedtalk_data_loader import TedtalkLoader
from src.news.news_data_extractor import NewsExtractor
from src.news.news_data_trannsformer import NewsTransformer




pre_processor = PreProcessor()
inference_processor = InferenceProcessor()
post_processor = PostProcessor()

# options = PipelineOptions(
#    direct_num_workers = 4,
#    direct_running_mode = "multi_processing"
# )


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

if __name__ == '__main__':
    # run()
    print("===Start Pipeline===")
    print("===Start Pre-Process===")
    
    res = pre_processor.process(element = "")

    print("===Start Inference Process===")
    res1 = inference_processor.process(res)

    print("===Start Sink Process===")
    res2 = post_processor.process(res1)