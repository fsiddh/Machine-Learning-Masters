def task1_2():
    #   List of numbers which are divisible by 7 and not by 5
    x = []

    for i in range(2000, 3001):
        if i % 7 == 0 and i % 5 != 0:
            x.append(i)
        else:
            continue

    print("Numbers which are divisible by 7 and not by 5 are:", end="\n" + str(x))


task1_2()
