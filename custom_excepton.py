# Custom exception example

class NegativeError(Exception):
    pass

try:
    num = int(input("Enter number: "))
    if num < 0:
        raise NegativeError("Negative number not allowed")
except NegativeError as e:
    print(e)
finally:
    print("Execution completed")