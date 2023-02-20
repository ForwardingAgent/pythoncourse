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

n = int(input())
lst = []
for _ in range(n):
    s = input()
    lst.append(s)
m = input()
for w in lst:
    if m.lower() in w.lower():
        print(w)