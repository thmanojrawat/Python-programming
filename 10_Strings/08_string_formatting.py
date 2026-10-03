# String formatting

name = "Alice"
age = 25

print("My name is %s and I am %d years old." % (name, age))

print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))
print("My name is {name} and I am {age} years old.".format(name="Bob", age=30))

print(f"My name is {name} and I am {age} years old.")
