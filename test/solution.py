equation = open('input.txt', 'r', encoding='utf8')

print(equation.read())
equation = str(equation.read())

# заменяем '=' на '==', в будущем это упростит код
for i in equation:
    print(equation)
# a = equation.index('=')
# first=equation[:a+1]
# second=equation[a:]
# equation =first+second

print(equation)


def replace_all(text, srch, repl):
    for i in range(0, len(srch)):
        text = text.replace(srch[i], repl[i])
    return text


letters = []

for l in equation:
    if l not in ('+', '='):
        if l not in letters:
            letters.append(l)

tops, counters = [], []
for i in range(0, len(letters)):
    tops.append(10 - i)
    counters.append(0)

canExit = False
while (not (canExit)):

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    substs = []
    for i in range(0, len(tops)):
        substs.append(numbers[counters[i]])
        del numbers[counters[i]]

    text = replace_all(equation, letters, substs)
    try:
        if eval(text):
            print(text)
            # останавливаем код
            break
    except:
        None

    N = 0
    inc = 1
    while (N < len(counters) and inc > 0):
        counters[N] += inc
        inc = 0
        if (counters[N] == tops[N]):
            counters[N] = 0
            inc = 1
            N += 1

    canExit = True
    for i in range(0, len(tops)):
        canExit &= (counters[i] == tops[i] - 1)
# убираем двойной пробел
# a=[]
# for i in text:
# a.append(i)
# a.remove('=')
# a=(" ".join(a))
# b = a.split()
# b = ''.join(b)
# print((b))
print(equation)
y = open('output.txt', 'w')
y.write(str(equation))



