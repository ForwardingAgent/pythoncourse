# https://replit.com/@NikolayPodkopae/boilerplate-mean-variance-standard-deviation-calculator-1#main.py
import numpy as np
from collections import defaultdict


def calculate(lst):
    if len(lst) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        arr_flattened = np.array(lst)
        arr = arr_flattened.reshape(3, 3)
        d = {}
        d['mean'] = d.get('mean', []) + [list(arr.mean(axis=0))]
        d['mean'] = d.get('mean', []) + [list(arr.mean(axis=1))]
        d['mean'] = d.get('mean', []) + [(arr_flattened.mean())]
        d['variance'] = d.get('variance', []) + [list(arr.var(axis=0))]
        d['variance'] = d.get('variance', []) + [list(arr.var(axis=1))]
        d['variance'] = d.get('variance', []) + [(arr_flattened.var())]
        d['standard deviation'] = d.get('standard deviation', []) + [list(arr.std(axis=0))]
        d['standard deviation'] = d.get('standard deviation', []) + [list(arr.std(axis=1))]
        d['standard deviation'] = d.get('standard deviation', []) + [(arr_flattened.std())]
        d['max'] = d.get('max', []) + [list(arr.max(axis=0))]
        d['max'] = d.get('max', []) + [list(arr.max(axis=1))]
        d['max'] = d.get('max', []) + [(arr_flattened.max())]
        d['min'] = d.get('min', []) + [list(arr.min(axis=0))]
        d['min'] = d.get('min', []) + [list(arr.min(axis=1))]
        d['min'] = d.get('min', []) + [(arr_flattened.min())]
        d['sum'] = d.get('sum', []) + [list(arr.sum(axis=0))]
        d['sum'] = d.get('sum', []) + [list(arr.sum(axis=1))]
        d['sum'] = d.get('sum', []) + [(arr_flattened.sum())]
        calculations = d

    return print(calculations)


calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
