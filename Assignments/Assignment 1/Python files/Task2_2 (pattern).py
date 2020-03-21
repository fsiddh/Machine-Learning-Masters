def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end="")
        print(end="\n")

    for p in range(n - 1, 0, -1):
        for q in range(p, 0, -1):
            print("*", end="")
        print("\n")


# Number of asterisk a user wants
x = int(input("Enter the number of asterisk's you want in your middle row: "))
pattern(x)
