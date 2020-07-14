# 列表声明
import random

movies = ['one', 'two', 'three', 'four']

# 元素获取
print(movies[0])

# 列表遍历
for i in movies:
    print(i, end='  ')
print()
print('-------------')
for i in range(len(movies)):
    print(i, movies[i])

# 列表元素更改

brands = ['huawei', 'xiaomi', 'dell', 'hp', 'apple', '神州', '游戏本']
for i in range(len(brands)):
    if '神州' in brands[i]:
        brands[i] = 'shenzhou'
        break
print(brands)

# 元素的删除
del brands[-1]
print(brands)

l = len(brands)
i = 0
while i < l:
    if 'x' in brands[i] or 'd' in brands[i]:
        del brands[i]
        l -= 1
    else:
        i += 1
print(brands)

# 列表切片

superstar = ['杨幂', '刘诗诗', '赵丽颖', 'hhh', 7, 9, 0, ['abc', 'def']]
print(superstar[2:5])  # 截取的结果也是一个列表
print(superstar[-1][0])

#  创建一个空列表

grils = []

# 列表追加元素
# append() 末尾追加
# extends() 把一个列表加到另外一个列表里
# insert() 指定位置插入

# while True:
#     name = input('请输入美女名字：')
#     grils.append(name)
#     if name == 'quit':
#         break
# print(grils)

# 产生10 个随机数保存到列表里


numlist = []
num = 0

while num < 10:
    ran = random.randint(1, 100)
    if ran not in numlist:
        numlist.append(ran)
        num += 1
print(numlist)

# 找出列表的最大值
print("-------------求最大值------------------")
print("----------方法一------------")
print(max(numlist))
print(min(numlist))
print(sum(numlist))
print("-----------方法二--------------")
max_value = numlist[0]
min_value = numlist[0]
suma = 0
for var in numlist:
    suma += var
    if var > max_value:
        max_value = var

    if var < min_value:
        min_value = var
print("最大值是：", max_value)
print("最小值是：", min_value)
print("总和：", suma)
