# else with loops

for i in range(3):
    print(i)
else:
    print("Loop completed without break")

print("---")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will not print because the loop broke early.")
