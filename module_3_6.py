data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def func(*args):
    summ = 0
    for elem in args:
        if isinstance(elem,str):
            summ += len(elem)
        elif isinstance(elem,int):
            summ += elem
        elif isinstance(elem,dict):
            summ += func(list(elem.keys()))
            summ += func(list(elem.values()))
        elif isinstance(elem, list):
            summ += func(*elem)
        elif isinstance(elem,tuple):
            summ += func(*elem)
        elif isinstance(elem, set):
            summ += func(list(elem))
    return summ
print(func(data_structure))