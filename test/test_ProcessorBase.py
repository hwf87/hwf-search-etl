import sys
import pytest

sys.path.append("..")
from src.ProcessorBase import PreProcessor, InferenceProcessor, PostProcessor


class Test_PreProcessor:
    @pytest.mark.parametrize("", [])
    def test_process(self):
        """ """
        PreProcessor()


class Test_InferenceProcessor:
    @pytest.mark.parametrize("", [])
    def test_process(self):
        """ """
        InferenceProcessor()


class Test_PostProcessor:
    @pytest.mark.parametrize("", [])
    def test_process(self):
        """ """
        PostProcessor()
