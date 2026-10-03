# Accessing dictionary values

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student["name"])
print(student.get("age"))
print(student.get("phone", "Not available"))

print(student.keys())
print(student.values())
print(student.items())
