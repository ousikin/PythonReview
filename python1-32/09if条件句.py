import random

while True:
    userName = input('请输入用户名：')
    password = int(input('请输入密码：'))
    if userName == random.choice(('王志鑫', 'admin', 'tom')):
        if password == random.randint(1, 10):
            print('输入成功')
            break
    else:
        print('用户名或密码不正确，请重新输入')
