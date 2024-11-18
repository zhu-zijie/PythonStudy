# coding=utf-8
# @File: greenlet.py
# @Author: zijier
# @Desc: 开发协程的案例，一个任务是回答，一个任务是问
# @Date: 14:26 2024/04/13

from greenlet import greenlet


def ask(name):
    print(f"{name}:我要买个手提包！")
    b.switch('吕布')
    print(f"{name}:我想学个Python！")
    b.switch('吕布')


def answer(name):
    print(f"{name}:买买买！")
    a.switch()
    print(f"{name}:一定马上去学习！")


if __name__ == '__main__':
    a = greenlet(ask)  # 创建第一个协程
    b = greenlet(answer)  # 创建第二个协程
    a.switch('貂蝉')  # 每个函数只有在第一次切换的时候才需要传参数，后面不需要
