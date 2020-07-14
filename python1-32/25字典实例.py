print('*' * 10, '欢迎来到51job', '*' * 10)
database = []
while True:
    username = input('输入你的用户名：')
    password = input('输入你的密码：')
    repassword = input('输入你的密码：')
    email = input('输入你的邮箱：')
    tel = input('输入你的手机号：')
    # 定义一个字典
    user = {}
    user['username'] = username
    if repassword == password:
        user['password'] = password
    else:
        print('密码输入不正确')
        continue
    user['email'] = email
    user['tel'] = tel

    # 把用户保存到数据库
    database.append(user)
    answer = input('是否继续注册？y/n')
    if answer != 'y':
        break
print(database)