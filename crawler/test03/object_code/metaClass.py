# 使用type()函数创建一个Person类
# def func(self):
#     print("你吃了吗？")
#
#
# Person = type('Person', (object,), dict(say=func))
# p = Person()
# p.say()


# 元类
class PersonMetaClass(type):    # 所有的元类必须继承type
    def __new__(cls, name, bases, attrs):
        def func(self, words):
            print(f'我说{words}')

        attrs['say'] = func
        return type.__new__(cls, name, bases, attrs)


class Person(object, metaclass=PersonMetaClass):
    def say(self, words):
        pass


# 创建Person类的实例
p = Person()
p.say('hello')
print(type(p))
print(type(Person))
