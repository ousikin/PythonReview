sumc = 0
i = 1
while i <= 100:
    sumc += i
    i = i + 1
print(sumc)

ceng = 1
while ceng <= 5:
    count = 1
    while count <= ceng:
        print('*', end=' ')
        count += 1
    ceng += 1
    print()

num1 = 1
while num1 <= 9:
    num2 = 1
    while num2 <= num1:
        print(num1, 'x', num2, '=', num1 * num2, end='  ')
        num2 += 1
    num1 += 1
    print()
