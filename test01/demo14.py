# coding=utf-8
# @File: demo14.py
# @Author: zijier
# @Desc: 
# @Date: 11:27 AM 2024/03/18

class Student():
    # 首尾下划线标表示特殊的方法，系统定义
    def __init__(self, name, age, gender):
        self._name = name  # 以单下划线开头，表示受保护的成员，只能类本身和子类访问
        self.__age = age  # 以双下划线开头，表示私有的，只能类本身使用
        self.gender = gender  # 普通的实例属性，在类的内部外部以及子类都可以访问

    def _fun1(self):  # 以单下划线开头，表示是受保护的方法
        print('子类和本身都可以访问！')

    def __fun2(self):  # 以双下划线开头，表示的是私有的
        print('只有定义的类可以访问！')

    # 普通的实例方法，在类的外部使用对象名打点访问，在类的内部使用self打点访问
    def show(self):
        self._fun1()  # 类本身访问受保护的方法
        self.__fun2()  # 类本身访问私有的方法
        print(self._name)  # 类本身访问受保护的实例属性
        print(self.__age)  # 类本身访问私有的实例属性


if __name__ == '__main__':
    stu = Student('张三', 20, '男')
    print(stu._name)
    stu._fun1()
    stu.show()
