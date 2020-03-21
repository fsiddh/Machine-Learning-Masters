"""def filter_long_words(iterable, n):
    x = []
    x = [x.append(i) for i in iterable if len(i) > n]
    for i in iterable:
        if len(i) > n:
            x.append(i)

    return x


l = ["Happy", "Sad", "Action", "Dance", "Artificial", "Machine"]
print(filter_long_words(l, 5))"""


def filter_long_words(iterable, n):
    x = []
    for i in iterable:
        if len(i) > n:
            x.append(i)
    return x


l = ["Happy", "Sad", "Action", "Dance", "Artificial", "Machine"]
result = filter_long_words(l, 5)
print(result)
