dict1 = {'1': '张三', '2': 'tom', '3': 'join', '4': 'jack'}
# 根据key 获取value
print(dict1['1'])

for key in dict1:
    print(key, dict1[key])

# 字典里的函数
# items()  values()  keys()

print(dict1.items())  # dict1.items()输出一个列表
# [('1', '张三'), ('2', 'tom'), ('3', 'join'), ('4', 'jack')]
# 用for循环实际上是对元组进行了一个拆包的过程
for key, value in dict1.items():
    print(key, value)

# values 取出字典中所有的值
for i in dict1.values():
    print(i)

# keys 取出字典中所有的键
for i in dict1.keys():
    print(i)
