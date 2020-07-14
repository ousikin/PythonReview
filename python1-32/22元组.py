'''
1.定义 tuple()
2.一个元素 tuple1 = (1,) 必须加 ","
'''

# 3. tuple() 不能进行增删改
# 想要增tuple(list()) 把列表转为元组

# 4 元组的查询[]

# 5 元组的常用函数
tuple1 = (1, 2, 5, 2, 3, 4, 8)
# count
print('2出现的次数', tuple1.count(2))
# index
print('第一次出现2的下标', tuple1.index(2))
