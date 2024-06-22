# 求列表的阶乘

def func1(num):
    if num == 1:
        return 1
    else:
        return num * func1(num - 1)

# func2就是高阶函数，它的参数就是函数本身。
def func2(lst, func):
    new_list = []
    for x in lst:
        new_list.append(func(x))
    return new_list


lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(func2(lst, func1))
