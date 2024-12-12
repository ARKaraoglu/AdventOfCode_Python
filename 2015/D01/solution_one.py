file = open("input.txt", "r")
contents = file.read()

floor = 0
for index in contents:
    if index == "(":
        floor += 1
    elif index == ")":
        floor -= 1
    else:
        continue

print(floor)
