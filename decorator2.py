from decorators import do_twice

@do_twice
def say_whee():
    print("whee!")

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def greeting(name):
    print('creating greeting..')
    return f'hi {name}'

# say_whee()
# greet("ram")
greeting("ram")

print(help(say_whee))

