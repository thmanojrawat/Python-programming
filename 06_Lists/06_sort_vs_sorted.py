# sort() vs sorted()

numbers = [4, 2, 1, 5, 3]

numbers.sort()
print("sort():", numbers)

numbers = [4, 2, 1, 5, 3]
new_list = sorted(numbers)

print("sorted():", new_list)
print("Original:", numbers)

result = numbers.sort()
print("Return value of sort():", result)
