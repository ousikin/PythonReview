'''
列表推导式格式：
[表达式 for 变量 in 旧列表]
[表达式 for 变量 in 旧列表 if 条件]
'''

names = ['ab', 'bbbbb', 'eeec', 'dfff', 'gggggge']
result = [i for i in names if len(i) > 3]
print(result)

result1 = [h for h in range(1, 100) if h % 3 == 0 and h % 5 == 0]
print(result1)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
newDict = {value: key for key, value in dict1.items()}
print(newDict)
