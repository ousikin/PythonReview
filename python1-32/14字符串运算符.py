# 字符串
a1 = 'hello'
a2 = "hello"
a3 = '''hello'''
print(a1 == a2)  # 比较的是内容

print(a1 is a2)  # 比较的是地址
print(a2 == a3)
print(a2 is a3)

# b1 = input('请输入')
# b2 = input('请输入')
# print(b1 == b2)  # True
# print(b1 is b2)  # False

# 字符串的运算符
print(a1 + a2)  # +表示拼接
print(a1 * 4)  # *
print('a' in a1)  # in 在--里面
print('a' not in a1)  # not in 不在....里面
# % 字符串的格式化

# 字符串的切片
fileName = 'helloworld'  # 索引是从0开始
print(fileName[0])
print(fileName[0:])
print(fileName[0:5])  # 包前不包后
print(fileName[8:-1])
print(fileName[-5:-1])
print('--------------')
print(fileName[1:5:2])

# 字符串的逆序
# [::-1]
print(fileName[::-1])
