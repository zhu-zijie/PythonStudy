class Person(object):
    @property  # age属性暴露
    def age(self):
        return self._age

    @age.setter  # 当前age属性允许去赋值
    def age(self, age):
        if age >= 0 and age <= 88:
            self._age = age
        else:
            self._age = 0
            raise ValueError("age的值必须在0-88之间")

    # self_name表示受内部保护的，推荐使用getter个setter去访问
    @property  # 只能读
    def name(self):
        self._name = '张三'
        return self._name


if __name__ == '__main__':
    p = Person()
    p.age = 18  # 可以读可以写
    print(p.age)
    # p.name = '李四'   # 不能赋值
    print(p.name)
