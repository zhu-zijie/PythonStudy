# coding=utf-8
# @File: demo6.py
# @Author: zijier
# @Desc: 
# @Date: 8:13 PM 2024/03/13

# # 个数可变的位置传参，返回值为元组
# def fun(*args):
#     print(args)
#     print(args[0])
#
#
# fun(10)
# fun(10, 20)
# fun(10, 20, 30)
#
#
# # 个数可变的关键字传参，返回值为字典
# def fun(**args):
#     print(args)
#
#
# fun(a=10)
# fun(a=10, b=20)
# fun(a=10, b=20, c=30)

def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


# 函数的调用
fun(10, 20, 30)
lst = [40, 50, 60]
fun(*lst)  # 在函数调用时，将列表中的每一个元素转化为位置实参传入

fun(a=100, b=200, c=300)
dic = {'a': 400, 'b': 500, 'c': 600}
fun(**dic)  # 在函数调用时，将字典中的键值对转化为关键字实参传入
