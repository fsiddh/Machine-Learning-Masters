def task1_3(x,y):
    l_f = x[::-1]
    l_l = y[::-1]

    print(l_f + " " + l_l)


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
task1_3(first_name, last_name)