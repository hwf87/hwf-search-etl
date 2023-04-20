import sys
import pytest

sys.path.append("..")
from src.ProcessorBase import PreProcessor, InferenceProcessor, PostProcessor


class Test_PreProcessor:
    def test_process(self):
        """ """
        PreProcessor()
        assert 1 == 1


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
