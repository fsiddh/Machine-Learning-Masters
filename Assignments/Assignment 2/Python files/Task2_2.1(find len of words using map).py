def map_len_words(iterable):
    return list(map(len, iterable))


l = ["hello", "everyone", "Ron", "Harry"]
result = map_len_words(l)
print(result)
