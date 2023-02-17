t = int(input())
for n in range(1, t + 1):
    # if n == 1:
        # print('NO')
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
            if len(lst) > 2 or n == 1:
                # print('NO')
                lst = []
                break
    if len(lst) == 2:
        # print('YES')
        print(i, end=' ')