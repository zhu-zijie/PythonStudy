# coding=utf-8
# @File: demo7.py
# @Author: zijier
# @Desc: 
# @Date: 9:09 PM 2024/03/13

class Student:  # Student为类的名称，由一个或多个单词组成，每个单词的首字母大写
    native_pace = '湖北'  # 直接写在类里的变量成为类属性，被该类的所有的对象所共享

    def __init__(self, name, age):
        self.name = name  # self.name为实例属性
        self.age = age

    # 实例方法
    def eat(self):
        pass

    # 静态方法，使用类名直接访问的方法
    @staticmethod
    def sm():
        pass

    # 类方法，使用类名直接访问的方法
    @classmethod
    def cm(cls):
        pass


# 在类之外定义的称为函数，在类之内定义的成为方法
def drink():
    pass


stu1 = Student("张三", 20)    # 对象名.方法名()
stu1.eat()
Student.eat(stu1)   # 类名.方法名(类的对象),实际上就是方法处的self

#
