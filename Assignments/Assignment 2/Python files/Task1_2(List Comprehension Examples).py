# List Comprehension = [expression condition]

# 1
given_word = "ACADGILD"
result = [letters for letters in given_word]
print(result)

# 2
given_list = ['x','y','z']
# First for loop is outer loop and the second one is inner loop
# After the expression the first statement is always the outer condition/fn followed by inner condition/fn
# It means first the expression will run for all the values of number given first value of item
result = [items*number for items in given_list for number in range(1, 5)]
print(result)

# 3
result = [items*number for number in range(1,5) for items in given_list]
print(result)

# 4
given_list = [2,3,4]
result = [[i+j] for i in given_list for j in range(3)]
print(result)

# 5
given_list = [2,3,4,5]
result = [[i+number for i in given_list] for number in range(4)]
print(result)

# 6
given_list = [1,2,3]
result = [(j,i) for i in given_list for j in given_list]
print(result)