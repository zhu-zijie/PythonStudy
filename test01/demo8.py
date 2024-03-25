# coding=utf-8
# @File: demo8.py
# @Author: zijier
# @Desc: 
# @Date: 10:13 PM 2024/03/13

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭！')


stu1 = Student("张三", 20)
stu2 = Student("李四", 30)
# 为stu1动态绑定性别属性
stu1.gender = "男"
print(stu1.name, stu1.age, stu1.gender)
print(stu2.name, stu2.age)

# 为stu1动态绑定方法
def show():
    print("你很秀！")

stu1.show = show
stu1.show
