# 匿名函数
# 格式 lambda 参数1，参数2：运算

y = lambda a, b: print(a + b)
y(1, 2)


# 匿名函数可以做一个参数出现
def func(x, y, func):
    print(x, y)
    print(func)
    s = func(x, y)
    print(s)


func(1, 2, lambda a, b: a + b)
