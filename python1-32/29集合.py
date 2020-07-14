# 特点：set 无序不重复的元素
# 声明：set()
s1 = {1, 2, 3}
list1 = [1, 1, 1, 2, 3, 4, 4, 5, 5]
s2 = set(list1)
print(s2)

# 增删改查
# 增：add()  update()

s3 = set()
s3.add('aa')
s3.add('bb')
s3.add('cc')
print(s3)
s4 = ('dd', 'ee', 'ff')  # 把s4作为一个整体添加到s3中
s3.add(s4)  # {'bb', ('dd', 'ee', 'ff'), 'cc', 'aa'}
print(s3)
s3.update(s4)
print(s3)  # {'ee', 'ff', 'aa', ('dd', 'ee', 'ff'), 'dd', 'bb', 'cc'}

# 删
# remove()
s3.remove('dd')
print(s3)
# pop()
s3.pop()  # 删除第一个元素
# clear()
# discard() 删除没有的元素，不报错
