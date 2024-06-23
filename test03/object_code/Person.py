import types


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(object):
    # 只允许当前Student拥有name和sex属性
    __slots__ = ('name', 'sex')


if __name__ == '__main__':
    p = Person("张三", 22)
    Person.address = "武汉"
    # 1.可以动态的给对象p赋予一个新的对象属性
    p.sex = '男'

    # 2.可以给当前对象p动态的赋予一个新的对象函数
    def run(self, work):
        print(f"{self.name}正常完成的工作是{work}")
    # 给对象p添加一个实例（成员，对象）函数
    p.run = types.MethodType(run, p)
    p.run('学习')


    # 3.给Person类动态赋予一个类函数
    @classmethod
    def class_run(cls, work):
        print(f"类函数的work是{work}")
    Person.work = class_run
    p.work("学习Python")


    # 4.给Person类动态赋予一个静态函数
    @staticmethod
    def static_run(work):
        print(f"静态方法的work是{work}")
    Person.staticRun = static_run
    # p.staticRun("学习全栈！")
    Person.staticRun("学习全栈！")

    s = Student()
    s.name = "李四"
    s.sex = "女"
    # s.age = 18
    print(s.sex)

    