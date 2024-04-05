def outer_func(msg):
    message = msg
    def inner_func():
        print(f"{message} world")
    return inner_func

hi_func = outer_func('hi')
hi_func()

hello_func = outer_func('hello')
hello_func()