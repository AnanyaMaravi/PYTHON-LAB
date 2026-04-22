# Program to classify number as positive, negative, or zero

num = int(input("Enter a number: "))

# Nested if condition
if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")
