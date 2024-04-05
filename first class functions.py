# def square(x):
#     return x**2

# functions can be assigned to a variable
# # and then the variables can be used as functions
# f = square
# print(square(5))
# print(f(5))

# pass functions as arguments to another function
# def my_map(fun, args):  
#     # first class function
#     result = []
#     for i in range(len(args)):
#         result.append(fun(args[i]))
#     return result

# nums = [1,2,3,4]
# squares = my_map(square, nums)
# print(squares)

# return a function from a function
#  EX.1
# def logger(msg: str):
#     def log_message():
#         print(msg)
#     return log_message

# log_hi = logger('Hi!')
# log_hi()

# EX.2
def html_tag(tag: str):
    def wrap_text(msg: str):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline')
print_h1('Another Headline')

print_p = html_tag('p')
print_p('Test Paragraph')