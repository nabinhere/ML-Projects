# # Python program to 
# # demonstrate protected members 

# # Creating a base class 
# class Base: 
# 	def __init__(self): 

# 		# Protected member 
# 		self._a = 2

# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 

# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", 
# 			self._a) 

# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", 
# 			self._a) 


# obj1 = Derived() 

# obj2 = Base() 

# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 

# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 



# Python program to 
# demonstrate private members 

# Creating a Base class 
class Base: 
	def __init__(self): 
		self.a = "normal attribute"
		self._b = "protected attribute"
		self.__c = "Private attribute"

# Creating a derived class 
class Derived(Base): 
	def __init__(self): 

		# Calling constructor of 
		# Base class 
		Base.__init__(self) 
		print("Calling private member of base class: ") 
		print(self.__c) 


# Driver code 
obj1 = Base() 

# normal attribute can be accessed outside of class
print(obj1.a) 

# Though possible in python,
# protected attribute is accessible within the base class and 
# derived classes, but not in the derived class
print(obj1._b)

# private attributes are not accessible to derived classes as well
# this will raise an AttributeError
# print(obj1.__c)

# This will raise an error too
obj2  = Derived()
