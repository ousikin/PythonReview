# 闭包
# 在函数中提出的概念
'''
 闭包特点：1.在外部函数中定义了一个内部函数，
 2外部函数是有返回值的，
 3返回值是内部函数名
 4内部函数引用了外部函数的变量值

 格式：
 def 外部函数（）：
    ...
    def 内部函数（）：
    ...
    return 内部函数
    

 '''


def func():
    a = 100

    def inner_def():
        b = 10
        print(a, b)

    return a, inner_def


x, y = func()
y()  # 函数名加()表示调用函数
