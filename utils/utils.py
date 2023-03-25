import os
import logging

# def exception_handler(func):
#     """
#     Try catch template
#     """
#     def inner_function(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#             logging.DEBUG(f"MSG: {__name__}")
#         except Exception as e:
#             logging.error(f"{__name__} {e}")
#     return inner_function


# def logger(name: str):
#     def exception_handler(func):
#         def inner_function(*args, **kwargs):
#             try:
#                 func(*args, **kwargs)
#                 print(func.__name__)
#             except Exception as e:
#                 logging.error(f"{name} {e}")
#         return inner_function
#     return exception_handler

import functools

def log(logger: str):
    def exception_handler(func):
        def inner_function(*args, **kwargs):
            filename = os.path.basename(func.__code__.co_filename)
            try:
                func(*args, **kwargs)
                logger.debug(f"[DEBUG]==> File: {filename} | Function: {func.__name__}")
            except Exception as e:
                logger.error(f"[ERROR]==> File: {filename} | Function: {func.__name__} | MSG: {e}")
        return inner_function
    return exception_handler


# def log(logger: str):
#     @functools.wraps(func)
#     def inner_function(*args, **kwargs):
#         filename = os.path.basename(func.__code__.co_filename)
#         try:
#             func(*args, **kwargs)
#             logger.info(filename + ': begin ' + func.__name__)
#             logger.info(f"this is info!")
#         except Exception as e:
#             logger.error(f"{e}")
#     return inner_function


# import functools
# import logging

# logging.basicConfig(level = logging.DEBUG)
# logger = logging.getLogger()

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
#             raise e
#     return wrapper

# @log
# def foo():
#     raise Exception("Something went wrong")