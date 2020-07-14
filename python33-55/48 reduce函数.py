from functools import reduce

# reduce() 对可迭代对象进行加减乘除运算的操作
list1 = [7, 4, 5, 3, 7, 8, 9]

result = reduce(lambda x, y: x + y, list1)
print(result)

# filter() 过滤器
result = filter(lambda x: x > 6, list1)
print(list(result))

# sorted()
students = sorted(list1, key=lambda x: x)
print(students)
