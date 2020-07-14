import random

numlist = []
num = 0

while num < 10:
    ran = random.randint(1, 100)
    if ran not in numlist:
        numlist.append(ran)
        num += 1
print(numlist)

print("----------列表排序———————")

# 方法一：
newlist = numlist.sort()
print(numlist)

# 方法二：
# 参数reverse=True时，为降序排列
newlist1 = sorted(numlist, reverse=True)
print(newlist1)

# 方法三：
