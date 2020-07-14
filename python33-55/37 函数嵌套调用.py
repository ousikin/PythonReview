import random


def do_pass(n):
    str1 = 'hfdnskfv34f254yv7bidfafa750498509u'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(str1) - 1)
        code += str1[ran]
    return code


def login():
    username = input('请输入用户名：')
    password = input('请输入密码')
    code = do_pass(5)
    print('验证码是', code)
    code1 = input('请输入验证码')
    if code.lower() == code1.lower():
        if username == 'admin' and password == '123456':
            print('登录成果')
        else:
            print('输入密码或用户名不存在')
    else:
        print('验证码输入有误')


login()
