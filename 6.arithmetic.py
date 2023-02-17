def arithmetic_arranger(problems, arg=''):
    lst1, lst2, lst3, lst4 = '', '', '', ''
    if len(problems) > 5:
        return ('Error: Too many problems.')
    for v, i in enumerate(problems):
        i = i.split(' ')
        if len(i[0]) and len(i[2]) > 4:
            return ('Error: Numbers cannot be more than four digits.')
        if i[1] != '+' and i[1] != '-':
            return ("Error: Operator must be '+' or '-'.")
        if i[0].isdigit() is not True or i[2].isdigit() is not True:
            return ('Error: Numbers must only contain digits.')
        if len(i[0]) - len(i[2]) > 0:
            a = len(i[0])
        else:
            a = len(i[2])
        # a = len(i[0]) | len(i[2])  # определяем длинное число из 2
        # ' ' * (a - len(i[0])) - из определенной выше длины вычетаем длину числа и умножаем на пробел
        if v == len(problems) - 1:
            lst1 += '  ' + ' ' * (a - len(i[0])) + i[0]
        else:
            lst1 += '  ' + ' ' * (a - len(i[0])) + i[0] + '    '
        if v == len(problems) - 1:
            lst2 += i[1] + ' ' + ' ' * (a - len(i[2])) + i[2]
        else:
            lst2 += i[1] + ' ' + ' ' * (a - len(i[2])) + i[2] + '    '
        if v == len(problems) - 1:
            lst3 += '--' + '-' * a
        else:
            lst3 += '--' + '-' * a + '    '
    #lst1.append('  ' + ' ' * (a - len(i[0])) + i[0] + '    ')
    #lst2.append(i[1] + ' ' + ' ' * (a - len(i[2])) + i[2] + '    ')
    #lst3.append('--' + '-' * (len(i[2]) | len(i[0])) + '    ')
    if arg is True:
        for k, j in enumerate(problems):
            j = j.split(' ')
            if j[1] == '+':
                if len(i[0]) - len(i[2]) > 0:
                    a = len(i[0])
                else:
                    a = len(i[2])
                b = int(j[0]) + int(j[2])
                w = a + 2  # ширина столбца
                if len(str(b)) > a:
                    a = len(str(b))
                if k == len(problems) - 1:
                    lst4 += ' ' * (w - a) + str(b)
                else:
                    lst4 += ' ' * (w - a) + str(b) + '    '
            else:
                if len(i[0]) - len(i[2]) > 0:
                    a = len(i[0])
                else:
                    a = len(i[2])
                w = a + 2  # ширина столбца
                b = int(j[0]) - int(j[2])
                if b < 0:
                    w = w - 1
                if k == len(problems) - 1:
                    lst4 += ' ' * (w - a) + str(b)
                else:
                    lst4 += ' ' * (w - a) + str(b) + '    '     
        arranged_problems = lst1 + '\n' + lst2 + '\n' + lst3 + '\n' + lst4
        return arranged_problems
    else:
        arranged_problems = lst1 + '\n' + lst2 + '\n' + lst3
        return arranged_problems


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))