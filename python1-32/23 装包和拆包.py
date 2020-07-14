# 拆包
t1 = (1, 2, 3)
a, b, c = t1

print(a)
print(b)
print(c)

# 例1
t2 = (1, 2, 3, 4, 5)
d, *args, e = t2
print(d, e, args)
print(*args)

# 例2

t3 = (1,)
d, *args = t3
print(d, args)  # =>  1 []

# 装包  赋值可看成是装包
