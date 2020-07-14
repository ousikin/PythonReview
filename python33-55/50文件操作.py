# file = open(r'F:\p1\aa.docx', 'rb').read()
# print(file)

# ff = open(r'F:\p2\a.txt', 'wb').write(file)
# print('dd')

with open(r'F:\p1\aa.txt', 'rb') as file:
    file1 = file.read()
    with open(r'F:\p2\aa.txt', 'wb') as file3:
        file3.write(file1)
print('复制成功')
