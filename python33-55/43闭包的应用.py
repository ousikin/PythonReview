# 闭包用来制作计数器

def g_count():
    count = [0]

    def add():
        count[0] = count[0] + 1
        print('当前是第{}次访问'.format(count[0]))

    return add


add_sum = g_count()
add_sum()
add_sum()
add_sum()
