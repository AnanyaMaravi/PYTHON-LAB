# Program to find sum of first N natural numbers

n = int(input("Enter value of N: "))
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)
