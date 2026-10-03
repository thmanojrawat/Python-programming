# Creating dictionaries

student1 = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

student2 = dict(name="Bob", age=21, grade="B")

student3 = dict([
    ("name", "Charlie"),
    ("age", 22),
    ("grade", "A")
])

print(student1)
print(student2)
print(student3)
