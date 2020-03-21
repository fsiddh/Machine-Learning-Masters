def my_filter(fn, sequence):
    # Initializing an empty list
    final_list = []

    # Passing every item in the sequence through values,
    # then passing every value of values through the used function,
    # if the result of fn comes out to be true, appending the value of the sequence to the final_list
    for values in sequence:
        if fn(values):
            final_list.append(values)

    return final_list


# To test filter function
def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False


numbers = range(11)
x = my_filter(iseven, numbers)
print("Using filter, your even numbers are: \n", str(x))
