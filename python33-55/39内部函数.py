def func():
    n = 100
    list1 = [3, 4, 5, 6]

    def inner_fun(list1, n):
        for index, i in enumerate(list1):
            list1[index] += n
        list1.sort()
        print(list1)

    inner_fun(list1, n)


func()
