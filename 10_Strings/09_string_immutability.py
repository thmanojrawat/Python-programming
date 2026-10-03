# Strings are immutable

s = "Hello"

# s[0] = "h"  # TypeError

s2 = "h" + s[1:]

print("Original:", s)
print("New string:", s2)
