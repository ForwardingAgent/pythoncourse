import pandas as pd
import re


def length_stats(string):
    string1 = re.sub("[^А-Яа-я ]", "", string)
    lst = string1.lower().split()
    lst1 = set(lst)
    lst1 = sorted(lst1)
    len_lst1 = [len(i) for i in lst1]
    s = pd.Series(len_lst1, index=lst1)
    return s


print(length_stats('раму Мама, мыла!'))
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
