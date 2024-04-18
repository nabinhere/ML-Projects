import itertools

# my_list = [1,2,3]
# combinations  = itertools.combinations(my_list, 2)
# permutations = itertools.permutations(my_list, 2)

# print('Combinations:')
# for c in combinations:
#     print(c)

# print('Permutations:')
# for p in permutations:
#     print(p)

# combination is better for the following example
my_list = [1,2,3,4,5,6]
combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)
print([result for result in combinations if sum(result)==10])

# permutation is better for the following example
word = 'sample'
target_word = 'plmeas'
combinations = itertools.combinations(word, 6)
permutations = itertools.permutations(word, 6)

for p in permutations:
    if ''.join(p) == target_word:
        print("Match!")
        break
else:
    print("No Match!")