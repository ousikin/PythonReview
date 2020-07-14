list1 = [3, 4, 5, 6, 7, 8, 9]

result = map(lambda x: x + 3, list1)
print(list(result))

result1 = map(lambda y: y if y % 2 == 0 else y + 1, list1)
print(list(result1))
