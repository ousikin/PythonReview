massage = 'hello world'

# capitalize() 将字符串的第一个字符转化为大写
m1 = massage.capitalize()
print(m1)

# title() 每个单词的首字母大写
m2 = massage.title()
print(m2)

# upper 把小写转大写
m3 = massage[0:6].upper()
print(m3)

# lower 把大写转小写
m4 = massage.lower()
print(m4)

# len() 求字符串的长度
print(len(massage))

# find('查找的字符'，)

# replace() 替换
print(massage.replace(' ', '#'))

# encode编码  decode解码

# isalpha()判断字符串是否全都有字母组成
# isdigit() 判断是否字符串全部都是有字母组成

sum = 0
for n in range(3):
    num = input('请输入数字')
    if num.isdigit():
        sum += int(num)
print(sum)

# join
new_str = '-'.join('abc')
print(new_str)

# lstrip() 去掉左侧空格
stra = ' aax  nnx   bbx '
print(stra.lstrip())

# rstrip() 去掉右侧空格
print(stra.rstrip())

# trip() 去掉左右两侧空格
print(stra.strip())

# split() 分割字符串
print(stra.split('x', 3))

# count(args) 求args的个数
print('个数', stra.count('x'))
