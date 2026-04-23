# Program for list slicing and manipulation

lst = [10, 20, 30, 40, 50]

# Slicing
print("First 3 elements:", lst[:3])

# Add element
lst.append(60)
print("After append:", lst)

# Remove element
lst.remove(20)
print("After remove:", lst)

# Update element
lst[0] = 100
print("After update:", lst)
