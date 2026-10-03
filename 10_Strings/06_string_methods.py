# Common string methods

text = " Hello, Python! "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("Python", "World"))
print(text.split(","))

words = ["Python", "is", "easy"]
print(" ".join(words))

print(text.find("Python"))
print(text.count("l"))
print(text.startswith(" Hello"))
print(text.endswith(" "))
