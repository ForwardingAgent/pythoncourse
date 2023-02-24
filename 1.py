'''lst = ''
ans = [0]
while (s := input()) != 'ФИНИШ':
    lst += s
t = set(lst)
for i in t:
    r = s.count(i)
    if r == ans[]:
        ans.append(r)
    elif r > ans[0]:
        ans[0] = r
print(r)'''

'''n = int(input())
lst = []
for _ in range(n):
    s = input()
    lst.append(s)
m = input()
for w in lst:
    if m.lower() in w.lower():
        print(w)'''

'''s = input()
s = s.replace(' ', '').lower()
s1 = s[::-1]
count = 0
for i in range(len(s)):
    if s[i] == s1[i]:
        count += 1
    else:
        print('NO')
        break
if count == len(s):
    print('YES')'''

'''a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print('Infinite solutions')
else:
    D = b ** 2 - 4 * a * c
    if a == 0:
        if D == 0:
            print(0)
        else:
            print(f'{D:.2f}')
    else:
        if D > 0:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            if x1 > x2:
                print(f'{x2:.2f}', f'{x1:.2f}')
            else:
                print(f'{x1:.2f}', f'{x2:.2f}')
        elif D == 0:
            x1 = (-b) / (2 * a)
            print(f'{x1:.2f}')
        else:
            print('No solution')'''

l = int(input())
string = ''
n = int(input())
for i in range(n):
    s = input()
    string = string + '\n' + s
f = string[:(l - 3)] + '...'
f1 = string[:(l - 3 + f.count('\n'))] + '...'
print(f1)
