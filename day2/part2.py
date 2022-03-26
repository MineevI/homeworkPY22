with open('input1.txt', 'r') as file:
    input = file.read()

ribbon = 0

for line in input.split('\n'):
    (w, h, d) = [int(x) for x in line.split('x')]
    areas = [w*h, w*d, h*d]
    perims = [2 * x for x in [w+h, w+d, h+d]]
    ribbon += min(perims) + w*h*d
print("Ribbon: %s" % ribbon)

file = open("output2.txt", "w")
file.write(str(ribbon))
file.close()