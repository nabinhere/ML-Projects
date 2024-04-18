# def square_numbers(nums:list):
#     for num in nums:
#         yield(num*num)

# my_nums = square_numbers([1,2,3,4,5])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

my_nums = (x*x for x in [1,2,3,4,5]) #this will create a generator object
my_nums_list = list(my_nums)    #conversion of a generator into a list - not recommended
print(my_nums_list)
