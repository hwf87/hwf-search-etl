
import sys
sys.path.append("..")
import apache_beam as beam
from src.tedtalk.tedtalk_data_transformer import TedtalkTransformer
from src.tedtalk.tedtalk_data_extractor import TedtalkExtractor
from src.tedtalk.tedtalk_data_loader import TedtalkLoader

class PreProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()
      
    def process(self, element):
        """
        """
        TE = TedtalkExtractor()
        results = TE.extract()
        return results

class InferenceProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()
      
    def process(self, element):
        """
        """
        TT = TedtalkTransformer()
        results = TT.transform(element)
        return results
    
class PostProcessor(beam.DoFn):
    def __init__(self):
        super().__init__()
      
    def process(self, element):
        """
        """
        TL = TedtalkLoader()
        TL.load(element)
        return print("success")