dict1 = {'1': '张三', '2': 'tom', '3': 'join', '4': 'jack'}
# 删除
del dict1['1']
print(dict1)

# pop('key','没有键时，返回此默认值') dict的删除函数
result = dict1.pop('5', '没有此键')
print(result)

# popitem()随机删除字典中的键值对，一般从末尾开始删除
ruselt1 = dict1.popitem()
print(ruselt1)
print(dict1)

# clear()彻底删除


# 其他
# update() 相当于字典和字典的相加，如果原先有相同的键，值进行替换，没有则进行添加
dict1 = {1: 'w', 2: 'l', 3: 'y'}
dict2 = {1: 'e', 5: 'u'}
dict1.update(dict2)
print(dict1)
dict3 = {}

# fromkeys 列表变字典
list1 = [1, 2, 3, 4, 5]
dict4 = dict3.fromkeys(list1, 'aa')
print(dict4)
