# Removing dictionary items

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

del student["age"]
print(student)

grade = student.pop("grade")
print("Removed:", grade)

last_item = student.popitem()
print("Last item:", last_item)

student.clear()
print(student)
