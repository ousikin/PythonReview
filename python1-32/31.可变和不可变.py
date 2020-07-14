# 不可变：对象指向内存的值是不可变的
# 不可变类型：int  str   float tuple
# 不可变类型会开辟新内存，不会对原内存进行修改


# 可变： 对象指向内存的值是可变的
# 可变类型： list  dict  set 
# 可变类型不会开辟新内存，会对原内存进行修改

list1 = [1, 2, 3, 4]
print(id(list1))
list1.pop()
print(id(list1))

set1 = {1, 2, 3, 4}
print(id(set1))
set1.pop()
print(set1)
print(id(set1))
