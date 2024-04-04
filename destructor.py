class Person:
    def __init__(self, name, age) -> None:
        print("a person object created")
        self.name  = name
        self.age = age

    def __del__(self):
        print("destructor called, deleted object")

p1=  Person("Hari", 28)
p2 = Person("Phurba", 24)
print(f"name = {p1.name}")
print(f"age={p1.age}")
del p1
print(f"name = {p2.name}")
print(f"name = {p2.age}")
