# Nested if statement - 5 examples

age = 20
country = "India"

if age >= 18:
    if country == "India":
        print("Eligible to vote")
    else:
        print("Not eligible to vote in India")
else:
    print("Too young to vote")

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown user")

number = 15

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Not positive")

student = True
grade = 85

if student:
    if grade >= 80:
        print("Excellent student")
    else:
        print("Average student")
else:
    print("Not a student")

income = 50000
tax_paid = True

if income > 40000:
    if tax_paid:
        print("All good")
    else:
        print("Please pay taxes")
else:
    print("No tax needed")
