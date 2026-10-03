# Common list methods

numbers = [10, 20, 30]

numbers.append(40)
print("append:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.extend([50, 60])
print("extend:", numbers)

numbers.remove(15)
print("remove:", numbers)

removed = numbers.pop(0)
print("pop:", removed, numbers)

print("index of 30:", numbers.index(30))

numbers.append(30)
print("count of 30:", numbers.count(30))

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)

copied = numbers.copy()
print("copy:", copied)

numbers.clear()
print("clear:", numbers)
