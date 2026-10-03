# elif statement - 5 examples

grade = 72
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Fail")

day = "Wednesday"
if day == "Monday":
    print("Start of week")
elif day == "Wednesday":
    print("Midweek")
elif day == "Friday":
    print("Weekend coming")
else:
    print("Just another day")

num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

size = "M"
if size == "S":
    print("Small")
elif size == "M":
    print("Medium")
elif size == "L":
    print("Large")
else:
    print("Invalid size")

marks = 45
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 60:
    print("Good")
elif marks >= 50:
    print("Average")
else:
    print("Poor")
