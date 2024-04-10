import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"finished execution of {func.__name__} in {end_time-start_time: .4f} seconds")
        return value
    return wrapper_timer

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}:{repr(v)}" for k, v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__}({signature})")
        value = func(*args, kwargs)
        print(f"{func.__name__} returned ({repr(value)})")
        return value
    return wrapper_debug