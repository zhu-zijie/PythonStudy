class Person(object):
    def __init__(self, name):
        self.name = name
        # 斐波那契数列
        self.a, self.b = 0, 1

    # 用来定制对象的描述信息
    def __str__(self):
        return f"Person object (name :{self.name})"

    # person默认不是可迭代对象，变成一个可迭代对象，必须返回一个迭代器
    def __iter__(self):
        return self

    # 把对象当成列表看待
    def __getitem__(self, item):  # item是可能是下标，可能是一个切片
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0  # start默认值
            a, b = 1, 1
            lst = []
            for x in range(stop):
                if x >= start:
                    lst.append(a)
                a, b = b, a + b
            return lst

    # person变成一个迭代器
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

    # 当访问person对象中不存在的属性和函数时会抛出AttributeError，如果不想看到这个error则需要重写
    def __getattr__(self, item):
        if item == 'age':
            return 18
        elif item == 'eat':
            return lambda: print("eat函数执行！")

    def __call__(self, *args, **kwargs):
        print("person对象可以直接调用！")


if __name__ == '__main__':
    person = Person("张三")
    # print(person)
    # print(person.name)

    for n in person:
        print(n)

    # person有点类似于list
    print("下表为5的值为:", person[5])
    print("下表为5-10的值为:", person[5:10])
    person.eat()
    print(person.age)

    # 把person对象当函数直接调用，person对象==一个函数
    person()
    print(callable(person))  # person对象是不是可以调用的对象（函数）
