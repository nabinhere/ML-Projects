from decorators import do_twice

@do_twice
def return_greeting(name):
    print("creating greeting")
    return f"Hi {name}"

print(return_greeting("ram"))
# print(return_greeting.__name__)
