# print(dir(int))
# a = -5
# # print(a.__pow__(2))
# # print(a.__add__(6))
# # print(a.__abs__())
# # print(a.__neg__())

# the_list = ['a', 'b', 'c']
# print(the_list.__sizeof__())

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self):
        return f"Person {self.name}"
    
    def __add__(self, surname):
        return f"{self.name}" + f" {surname}"


p1 = Person("Ram")
print(p1)
print(p1+"khanal")