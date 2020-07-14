list1 = [{'a': 10, 'b': 20}, {'a': 20, 'b': 20}, {'a': 30, 'b': 20}, {'a': 40, 'b': 20}]
m = max(list1, key=lambda x: x['a'])
print(m)
