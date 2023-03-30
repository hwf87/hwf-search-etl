
import sys
sys.path.append("..")
import apache_beam as beam
from src.tedtalk.tedtalk_data_transformer import TedtalkTransformer
from src.tedtalk.tedtalk_data_extractor import TedtalkExtractor
from src.tedtalk.tedtalk_data_loader import TedtalkLoader
from src.news.news_data_extractor import NewsExtractor
from src.news.news_data_trannsformer import NewsTransformer
from src.news.news_data_loader import NewsLoader

class PreProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()
      
    def process(self, element):
        """
        """
        PRP = NewsExtractor()
        results = PRP.extract()
        return results

class InferenceProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()
      
    def process(self, element):
        """
        """
        IP = NewsTransformer()
        results = IP.transform(element)
        return results
    
class PostProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()
      
    def process(self, element):
        """
        """
        POP = NewsLoader()
        POP.load(element)
        return print("success")