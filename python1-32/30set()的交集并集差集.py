s1 = {'aa', 'bb', 'cc', 'dd'}
s2 = {'aa', 'bb', 'cc', 'dd', 'ee'}

# 差集 -  difference()
s3 = s2 - s1
s4 = s2.difference(s1)
print(s3)
print(s4)

# 交集 & intersection()
s5 = s1 & s2
print(s5)
s6 = s1.intersection(s2)
print(s6)

# 并集 | union()
s7 = s1 | s2
print(s7)
s8 = s1.union(s2)
print(s8)
