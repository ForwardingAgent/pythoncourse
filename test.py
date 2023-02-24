a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print('Infinite solutions')
else:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        if x1 == x2:
            print(f'{x1:.2f}')
        elif x1 > x2:
            print(f'{x2:.2f}', f'{x1:.2f}')
        else:
            print(f'{x1:.2f}', f'{x2:.2f}')
    else:
        print('No solution')


# Моя первая супер-пупер программа
'''n = int(input())
count = 0
for i in range(n):
    m = int(input())
    for t in range(1, m):
        if m % t == 0 and m != 1:
            count += 1
        else:
            continue
print(count)'''
'''
n = int(input())
m = int(input())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(m * i, end='')
    print()'''

'''lst = []
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        lst.append(i)
        if len(lst) > 2 or n == 1:
            print('NO')
            break
if len(lst) == 2:
    print('YES')'''

'''lst = []
n = int(input())
if n == 1:
    print('NO')
for i in range(2, n):
    if n % i == 0:
        lst.append(i)
        if len(lst) == 1:
            print('NO')
            break
if len(lst) == 0 and n != 1:
    print('YES')'''


