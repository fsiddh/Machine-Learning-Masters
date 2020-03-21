words = []
n = int(input("Enter number of words you want to enter:"))
for i in range(n):
    # Words to add in the list
    x = input("Enter the words one by one:")
    words.append(x)

# sorted(iterable, key, reverse)
# iterable is basically sequence of nums or words that need to be sorted, it can be of any type ex. list/tuple etx
# key sets the basis for sorting, for ex in this case it's length
# reverse if set true, it sorts in reverse order
result = sorted(words, key=len)

# took the last word as it'll be the longest word as the list is sorted length wise
print("Your longest word amongst ", words," is ", result[-1], end=".")