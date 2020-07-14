# dictionary 字典
'''
字典特点：
    1.符号{}
    2.关键字 dict
    3.保存的元素 {key ,value}

'''

# 定义：空字典
dict1 = {}
dict2 = dict()

# 定义一个字典
dict3 = {1: 'wzx', 2: 'll', 3: 'lx'}

# 转字典
dict4 = dict([(1, 2), (2, 3)])
print(dict4)

# 以下为错误案例
# dict5 = dict([(1, 2, 3), (2, 3)])

# 字典的增删改查
# 增加和修改

dict6 = {}
dict6['name'] = 'wzx'
dict6['age'] = 5
print(dict6)
# 没有key ,实现添加  有相同的key ,实现更改 key在字典中是唯一的
dict6['name'] = 'lxy'
print(dict6)
