# sort() vs sorted()

numbers = [4, 2, 1, 5, 3]

numbers.sort()
print("sort():", numbers)

numbers = [4, 2, 1, 5, 3]
new_list = sorted(numbers)

print("sorted():", new_list)
print("Original:", numbers)

tuple_data = (3, 1, 4)
print("sorted(tuple):", sorted(tuple_data))

# tuple_data.sort()  # Error because tuple has no sort() method
