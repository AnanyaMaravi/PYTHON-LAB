# Program to find largest of three numbers

# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Checking largest number
if a > b and a > c:
    print("Largest number is:", a)
elif b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
