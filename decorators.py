from functools import wraps

def do_twice(func):
    @wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        result = func(*args, **kwargs)
        func(*args, **kwargs)
        return result
    return wrapper_do_twice