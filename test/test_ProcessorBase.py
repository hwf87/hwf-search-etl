import sys
import pytest
sys.path.append("..")
from src.ProcessorBase import PreProcessor, InferenceProcessor, PostProcessor

class Test_PreProcessor:
    def test_process(self):
        """
        """
        assert 1==1

class Test_InferenceProcessor:
    @pytest.mark.parametrize("", [])
    def test_process(self):
        """
        """

class Test_PostProcessor:
    @pytest.mark.parametrize("", [])
    def test_process(self):
        """
        """

