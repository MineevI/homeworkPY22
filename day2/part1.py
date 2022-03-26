total = 0

with open("input1.txt") as f:
    content = f.readlines()

for c in content:
    (l, w, h)  = map (lambda x: int(x), c.split('x'))
    sides = [l * w, w * h, h * l]
    total += 2 * sum(sides) + min(sides)

print(total)

file = open("output1.txt", "w")
file.write(str(total))
file.close()