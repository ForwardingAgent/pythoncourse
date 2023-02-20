while (s := input()) == '':
    if '#' in s:
        g = s[:s.index('#')]
        if g == '':
            pass
        else:
            print(g)
    else:
        print(s)


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

'''
print(500)
m = 500
p = m
while (n := input()) != 'Угадал!':
    if n == 'Больше':
        m = round(m // 2)
        p = p + m
        print(p)
    elif n == 'Меньше':
        m = round(m // 2)
        p = p - m
        print(p)'''
