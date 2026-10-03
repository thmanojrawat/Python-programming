# Student gradebook

gradebook = {
    "Alice": {"Math": 85, "Science": 92, "English": 78},
    "Bob": {"Math": 88, "Science": 95, "English": 82},
    "Charlie": {"Math": 92, "Science": 90, "English": 85}
}

for student, grades in gradebook.items():
    average = sum(grades.values()) / len(grades)
    print(f"{student}: Average Grade = {average:.2f}")

gradebook["Diana"] = {
    "Math": 79,
    "Science": 85,
    "English": 88
}

gradebook["Alice"]["Math"] = 90

print(gradebook)
