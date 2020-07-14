# 自定义函数
# 函数名：动词加名词
import random


def generate_random(i, j):
    ran = random.randint(i, j)
    print(ran)


generate_random(1, 20)
print(generate_random(1, 20))
print(id(generate_random(1, 20)))
