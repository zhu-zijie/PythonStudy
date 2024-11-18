# coding=utf-8
# @File: demo9.py
# @Author: zijier
# @Desc: 
# @Date: 8:26 PM 2024/03/14

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        super().info()
        print(self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, teach_yaer):
        super().__init__(name, age)
        self.teach_year = teach_yaer

    def info(self):
        super().info()
        print(self.teach_year)


stu = Student("张三", 20, 1001)
stu.info()
teacher = Teacher("李四", 40, 10)
teacher.info()
