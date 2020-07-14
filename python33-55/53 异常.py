'''
    try:
        可能出现异常的代码
    except:
        如果有异常执行的代码
    finally:
        无论是否有异常都会执行的代码


'''


def add(a, b):
    try:
        return a / b
    except:
        print('除数不能为0')

    finally:
        print('你好啊')


c = add(1, 0)
print(c)
