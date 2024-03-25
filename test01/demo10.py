# coding=utf-8
# @File: demo10.py
# @Author: zijier
# @Desc: 
# @Date: 8:43 PM 2024/03/14

class Animal(object):
    def eat(self):
        print("动物会吃！")


class Dog(Animal):
    def eat(self):
        print("狗会吃骨头！")


class Cat(Animal):
    def eat(self):
        print("猫会吃鱼！")


class Person:
    def eat(self):
        print("人吃饭！")


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
