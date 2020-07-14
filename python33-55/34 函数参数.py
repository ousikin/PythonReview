# 可变参*args 返回一个元组
def add(a, *args):
    for i in args:
        a += i


print(add(1, 3, 4, 5))

# 关键字参 ： key =value  **kwargs 返回一个字典
dict1 = {'a': 1, 'b': 2, 'c': 3}


def plus(**kwargs):
    return kwargs


# **dict1 相当于把字典拆成 a=1,b=2,c=3
print(plus(**dict1))
