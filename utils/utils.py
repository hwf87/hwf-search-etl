import os
import logging
from typing import Callable


def get_logger(name: str) -> logging:
    """ """
    logger = logging.getLogger(f"{name}")
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "time: %(asctime)s | funcName: %(funcName)s | line: %(lineno)d | level: %(levelname)s | message:{%(message)s}"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def log(logger: str) -> Callable:
    """ """

    def exception_handler(func: Callable):
        def inner_function(*args, **kwargs):
            filename = os.path.basename(func.__code__.co_filename)
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as e:
                logger.error(
                    f"[ERROR]==> File: {filename} | Function: {func.__name__} | MSG: {e}"
                )

        return inner_function

    return exception_handler
