# Functions for string and list operations

# String functions
def string_operations(text):
    print("Upper:", text.upper())
    print("Lower:", text.lower())
    print("Reversed:", text[::-1])

# List functions
def list_operations(lst):
    print("Original list:", lst)
    lst.append(100)
    print("After append:", lst)
    print("Sorted list:", sorted(lst))

# Main
text = input("Enter a string: ")
lst = [1, 5, 3, 2]

string_operations(text)
list_operations(lst)