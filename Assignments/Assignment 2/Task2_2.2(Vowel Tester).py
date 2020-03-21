def vowel_tester(charecter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        if i == charecter:
            return True
        else:
            return False


result = vowel_tester('a')
print(result)