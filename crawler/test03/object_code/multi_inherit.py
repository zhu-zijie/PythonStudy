class Father(object):
    def work(self):
        print("父亲在工作！")


class Mother(object):
    def work(self):
        print("母亲在工作！")


class Child(Father, Mother):  # 多继承
    def __init__(self, name):
        self.name = name

    def work(self):
        print("我在工作！")


if __name__ == '__main__':
    child = Child("张三")
    child.work()  # 如果多个父类中有同样的函数，按照优先级来调用
