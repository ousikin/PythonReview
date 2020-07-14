# 占位符的格式化输出
name = 'Tom'
age = 18
name1 = 'Jerry'
name2 = 'jack'
print('我的的年龄是%d' % age)
print('你好%s我是%d' % (name, age))
print('我的名字是%s,我明年是%d' % (name, age + 1))
print('%s的朋友是%s和 %s ' % (name, name1, name2))

# format 格式化输出
print('{}的年龄是{}'.format(name, age))
