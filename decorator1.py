def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper function executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display()-> None:
    print('display function ran')

@decorator_function
def display_info(name:str, age:int) -> None:
    print(f'display_info ran with arguments {name} and {age}')

display()
display_info('ram', 25)

# decorated_display = decorator_function(display)
# decorated_display()

