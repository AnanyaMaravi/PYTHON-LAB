# Handling multiple exceptions

try:
    a = int(input("Enter number: "))
    print(10 / a)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")