# Nested dictionaries

school = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "courses": ["Math", "Physics"]
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "courses": ["Chemistry", "Biology"]
    }
}

print(school["student1"]["name"])
print(school["student2"]["courses"][0])

school["student3"] = {
    "name": "Charlie",
    "age": 21
}

print(school["student3"])
