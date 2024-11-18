def get_sum(*args):
    def tt():
        s = 0
        for n in args:
            s += n
        return s

    return tt


func = get_sum(1, 2, 3, 4, 5)
print(func())


# 得到左右小于100的质数

# 得到所有的奇数
def odd_num():
    n = 1
    while True:
        n += 2
        yield n


# 判断是否能被整除
def my_filter(x):
    return lambda n: n % x > 0


def zhiShu():
    yield 2
    g = odd_num()
    while True:
        x = next(g)  # 从生成器中拿到一个奇数
        g = filter(my_filter(x), g)  # 过滤之后的值再赋给g
        yield x


for n in zhiShu():
    if n < 100:
        print(n)
    else:
        break
