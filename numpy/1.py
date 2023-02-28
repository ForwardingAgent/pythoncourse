import numpy as np
from collections import defaultdict


def calculate(lst):
    arr_flattened = np.array(lst)
    arr = arr_flattened.reshape(3, 3)
    d = {}
    d['mean'] = d.get('mean', []) + [(arr.mean(axis=0))]
    print(d)
    d['mean'] = d.get('mean', []) + [(arr.mean(axis=1))]
    d['mean'] = d.get('mean', []) + [(arr_flattened.mean())]
    d['variance'] = d.get('variance', []) + [(arr.var(axis=0))]
    d['variance'] = d.get('variance', []) + [(arr.var(axis=1))]
    d['variance'] = d.get('variance', []) + [(arr_flattened.var())]
    d['standard deviation'] = d.get('standard deviation', []) + [(arr.std(axis=0))]
    d['standard deviation'] = d.get('standard deviation', []) + [(arr.std(axis=1))]
    d['standard deviation'] = d.get('standard deviation', []) + [(arr_flattened.std())]
    d['max'] = d.get('max', []) + [(arr.max(axis=0))]
    d['max'] = d.get('max', []) + [(arr.max(axis=1))]
    d['max'] = d.get('max', []) + [(arr_flattened.max())]
    d['min'] = d.get('min', []) + [(arr.min(axis=0))]
    d['min'] = d.get('min', []) + [(arr.min(axis=1))]
    d['min'] = d.get('min', []) + [(arr_flattened.min())]
    d['sum'] = d.get('sum', []) + [(arr.sum(axis=0))]
    d['sum'] = d.get('sum', []) + [(arr.sum(axis=1))]
    d['sum'] = d.get('sum', []) + [(arr_flattened.sum())]
    calculations = d

    return print(calculations)

'''def calculate(lst):
    arr_flattened = np.array(lst)
    print(arr_flattened)
    arr = arr_flattened.reshape(3, 3)
    print(arr)
    d = defaultdict(list)
    d['mean'].append(arr.mean(axis=0))
    print(d)
    d['mean'].append(arr.mean(axis=1))
    d['mean'].append(arr_flattened.mean())
    d['variance'].append(arr.var(axis=0))
    d['variance'].append(arr.var(axis=1))
    d['variance'].append(arr_flattened.var())
    d['standard deviation'].append(arr.std(axis=0))
    d['standard deviation'].append(arr.std(axis=1))
    d['standard deviation'].append(arr_flattened.std())
    d['max'].append(arr.max(axis=0))
    d['max'].append(arr.max(axis=1))
    d['max'].append(arr_flattened.max())
    d['min'].append(arr.min(axis=0))
    d['min'].append(arr.min(axis=1))
    d['min'].append(arr_flattened.min())
    d['sum'].append(arr.sum(axis=0))
    d['sum'].append(arr.sum(axis=1))
    d['sum'].append(arr_flattened.sum())
    calculations = d

    return print(calculations)'''


calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
