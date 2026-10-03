# Useful dictionary methods

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print("name" in student)
print("phone" in student)
print("Length:", len(student))

student_copy = student.copy()
print("Copy:", student_copy)

phone = student.setdefault("phone", "000-0000")
print("Phone:", phone)
print(student)
