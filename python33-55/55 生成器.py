# 得到生成器的方式
# 1.通过列表推导式得到生成器
# generator 生成器
# 生成器一
gen = (i * 3 for i in range(10))
print(gen)  # <generator object <genexpr> at 0x0000026FAD5E9970>
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
print('*' * 30)

while True:
    try:
        E = gen.__next__()
        print(E)
    except:
        print('打印结束')
        break


# 生成器二 借助函数完成
def func():
    n = 0
    while True:
        n += 1
        yield n


g = func()
print(g.__next__())
print(g.__next__())
print(g.__next__())
