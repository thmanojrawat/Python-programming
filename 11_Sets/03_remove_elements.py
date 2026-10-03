# Removing elements from sets

s = {1, 2, 3}

s.remove(2)
print(s)

s.discard(4)
print(s)

removed = s.pop()
print("Removed:", removed)
print(s)

s.clear()
print(s)
