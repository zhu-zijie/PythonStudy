class Person(object):
    # age 属性的值限制的范围是0-88
    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0 and age <= 88:
            self._age = age
        else:
            print("age的值必须在0-88之间")
            self._age = 0


if __name__ == '__main__':
    p = Person()
    # p.set_age(100)
    print(p.get_age())
