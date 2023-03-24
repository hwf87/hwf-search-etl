import logging

def exception_handler(func):
    """
    Try catch template
    """
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            logging.error(f"ERROR: {e}")
    return inner_function