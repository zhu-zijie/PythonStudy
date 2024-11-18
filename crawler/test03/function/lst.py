# 列表生成式
# lst = [1, 2, 3, 4, 5]
# lst = [x for x in range(1, 10)]
# print(lst)

# 生成器，对象，保存了产生元素的算法，同时记录游标的位置
# 遍历生成器里的元素1.通过next(g)或者g.__next__(),2.通过for来遍历
# 创建一个生成器
# 1.通过列表生成式来创建
# g = (x for x in range(1, 10))
# next(g)游标向下走一位，可能会抛异常：stopIteration
# print(g)
# print(next(g))

# for i in g:
#     print(i)


# 2.通过函数来创建
# 求固定次数的斐波那契数
def test1(times):
    a, b = 0, 1
    n = 0
    while n < times:
        yield b
        a, b = b, (a + b)
        n = n + 1
    return "done!"


# yield一般用于创建生成器，工作返回后面的变量值给生成器。yield没有返回值

# 无限次的斐波那契数
def test2():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, (a + b)

