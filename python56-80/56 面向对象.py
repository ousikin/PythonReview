# 世间万物皆对象
'''
面向对象
    类
    对象
    属性
    方法
    对象的共同特征为类的属性
    对象的共同动作为类的方法
'''
'''
    类
    规范： 类首字母大写 多个单词使用驼峰式命名
    类默认继承 Object
    格式： class 类名[(父类)]
    属性； 特征
    方法；动作
    
'''


# 属性部分
class People(object):
    name = ''  # 类属性
    sex = ''
    age = 1


wzx = People()
wzx.name = 'wangzhixin'  # 对象属性  先找自己空间的，然后再到类属性中找
wzx.sex = '男'  # 如果存在对象属性，则不会到类属性中找
wzx.age = 25
print(wzx)
print(wzx.age)
print(wzx.name)
print(wzx.sex)
