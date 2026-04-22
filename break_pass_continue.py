# Program to demonstrate break, continue, pass

for i in range(1, 6):

    if i == 3:
        continue   # skips 3

    if i == 5:
        break      # stops loop

    if i == 2:
        pass       # does nothing

    print(i)
