# 格式： for 变量名 in 集合：
#            语句


for i in range(3):
    print(i, 'hello')

name = 'li'
for i in range(5):
    print(name, '正在吃第', i + 1, '个馒头')

# pass 的用法

if 10 > 7:
    print('True')
else:
    pass
print('完事')

# 求和
sumq = 0
for i in range(1, 101):
    sumq += i
print(sumq)

# range的用法
print(sum(range(1, 101)))

print(sum(range(1, 5, 2)))

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
