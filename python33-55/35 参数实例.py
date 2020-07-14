def add(a, b, *args, **kwargs):
    print(a, b, args, kwargs)


add(1, 2)  # ->1 2 () {}
add(1, 2, 3, 4)  # ->1 2 (3, 4) {}
add(1, 2, d=6, e=5)  # -> 1 2 () {'d': 6, 'e': 5}
add(1, 2, 3, f=5)  # ->1 2 (3,) {'f': 5}
# add(1, 2, g=5, 7, 8) 错误案例，关键字参必须放后面


print('*' * 30)

list1 = [1, 2, 3, 4, 5]

dict1 = {1: 'a', 2: 'r', 3: 'h'}


def func(*args, **kwargs):
    print(args, kwargs)


func(list1)
func(*list1)
