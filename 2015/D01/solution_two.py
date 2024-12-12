file = open("input.txt", "r")
contents = file.read()

floor = 0
basementIndex = 0
for x in range(0, len(contents)):
    if contents[x] == "(":
        floor += 1
    elif contents[x] == ")":
        floor -= 1
    else:
        continue

    if floor == -1:
        basementIndex = x + 1
        break
print(basementIndex)
