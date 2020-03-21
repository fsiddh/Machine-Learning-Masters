def my_reduce(fn, sequence):

    # Initializing list to store the first element of the sequence
    result = sequence[0]

    # Now computing the first and second value to the fn,
    # this will go upto last value of the sequence
    for values in sequence[1:]:
        result = fn(result, values)

    return result


def product(x, y):
    return x*y


numbers = range(1, 11)
x = my_reduce(product, numbers)
print("Product of numbers using reduce function is:", str(x))