# Program to demonstrate read(), readline(), readlines()

file = open("sample.txt", "r")

print("Using read():")
print(file.read())

file.seek(0)

print("\nUsing readline():")
print(file.readline())

file.seek(0)

print("\nUsing readlines():")
print(file.readlines())

file.close()