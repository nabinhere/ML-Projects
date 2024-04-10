from decorators import timer, debug

# @timer
# def waste_time(num):
#     for _ in range(num):
#         sum([num**2 for num in range(1000)])

# waste_time(10000)

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy, {name}"
    else:
        return f"Howdy {name}, {age} already! you are growing up!"
    
print(make_greeting("Phurba", age = 25))
