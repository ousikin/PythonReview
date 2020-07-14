import os

# 获取当前文件的路径 绝对路径
'''
os.path 
os.path 获取当前文件的路径 绝对路径
os.path.join(path,'') 返回拼接后的路径

result=os.path.split(path) result[1] 可以得到文件名
os.path.splitext(path)  可以得到文件扩展名

os.path.getsize(path) 获取文件的大小，单位字节

'''

with open(r'F:\p1\aa.txt', 'rb') as file:
    print(file.name)
    file1 = file.read()

    path = os.path.dirname(__file__)
    result = os.path.join(path, 'a1.txt')
    with open(result, 'wb') as file3:
        file3.write(file1)
print('复制成功')
