from functools import wraps
import logging


def log_call(func):
    @wraps(func)
    def fn(*args, **kwargs):
        logging.info("Calling: " + func.__name__ + "("
                     + ", ".join(
                         [repr(a) for a in args] +
                         [a + "=" + repr(v) for a, v in kwargs.items()]
                         ) + ")")
        return func(*args, **kwargs)
    return fn