# Tuple to list and list to tuple

t = (10, 20, 30)

lst = list(t)
lst.append(40)

t = tuple(lst)

print(t)
