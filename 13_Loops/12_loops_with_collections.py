# Loops with list, tuple, set and dictionary

fruits = ["apple", "banana", "cherry"]
colors = ("red", "green", "blue")
numbers = {10, 20, 30}

print("List:")
for fruit in fruits:
    print(fruit)

print("Tuple:")
for color in colors:
    print(color)

print("Set:")
for number in numbers:
    print(number)

print("Dictionary:")
student = {"name": "Alice", "age": 20, "grade": "A"}

for key, value in student.items():
    print(key, ":", value)
