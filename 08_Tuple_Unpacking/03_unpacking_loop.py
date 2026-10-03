# Tuple unpacking in a loop

students = [
    ("Ali", 90),
    ("Sara", 85),
    ("John", 78)
]

for name, marks in students:
    print(f"{name} scored {marks}")
