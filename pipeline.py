import sys
import apache_beam as beam

sys.path.append("..")
from utils.utils import log, get_logger
from src.ProcessorBase import (
    PreProcessor,
    InferenceProcessor,
    PostProcessor,
    BeamPreProcessor,
    BeamInferenceProcessor,
    BeamPostProcessor,
)

logger = get_logger(name=__name__)


@log(logger)
def beam_runner(data_source: str) -> None:
    """ """
    beam_pre_processor = BeamPreProcessor()
    beam_inference_processor = BeamInferenceProcessor()
    beam_post_processor = BeamPostProcessor()
    with beam.Pipeline() as pipeline:
        (
            pipeline
            | "Trigger" >> beam.Create([data_source])
            | "Pre-Process" >> beam.ParDo(beam_pre_processor)
            | "Inference" >> beam.ParDo(beam_inference_processor)
            | "Post-Process" >> beam.ParDo(beam_post_processor)
        )
    logger.info(f"====BEAM RUNNER DONE====")


@log(logger)
def local_runner(data_source: str) -> None:
    """ """
    pre_processor = PreProcessor()
    inference_processor = InferenceProcessor()
    post_processor = PostProcessor()
    pipe = pre_processor.process(source=data_source)
    pipe = inference_processor.process(element=pipe[0])
    post_processor.process(element=pipe[0])
    logger.info(f"====LOCAL RUNNER DONE====")


if __name__ == "__main__":
    runner_mode = sys.argv[1]  # ["local", "beam"]
    data_source = sys.argv[2]  # ["houzz", "news", "tedtalk"]
    logger.info(f"Runner Mode: {runner_mode}")
    logger.info(f"Data Source: {data_source}")
    if runner_mode == "local":
        local_runner(data_source=data_source)
    elif runner_mode == "beam":
        beam_runner(data_source=data_source)
    else:
        logger.warning(f"====Can Not Find Runner Mode: {runner_mode}=====")
