def global_func(b, c):
    a = 5

    def inner_fun():
        d = a + b + c

        print(d)

    return inner_fun


x = global_func(2, 3)
x()
