a = 100


def pb():
    b = 299

    def inner_pb():
        global a  # 内部函数调用全局变量
        nonlocal b  # 内部函数调用外部函数中的变量
        c = 200
        a += 100
        b += 200

        print(a, b, c)

    inner_pb()


pb()
