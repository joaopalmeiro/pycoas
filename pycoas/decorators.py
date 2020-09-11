from functools import wraps
from time import perf_counter


def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = perf_counter()
        value = func(*args, **kwargs)
        end = perf_counter()
        elapsed_time = end - start
        print(f"⏰ Elapsed time: {elapsed_time:0.4f} seconds.")
        return value

    return wrapper_timer
