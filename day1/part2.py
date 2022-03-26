total = 0
pos = 1

with open("input1.txt") as f:
    content = f.readlines()

for c in content[0]:
    if c == '(':
        total += 1

    elif c == ')':
        total -= 1

    if total == -1:
        break

    pos += 1

print (pos)
file = open("output2.txt", "w")
file.write(str(pos))
file.close()