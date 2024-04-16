# coding=utf-8
# @File: gevent.py
# @Author: zijier
# @Desc: 开发协程的案例，一个任务是回答，一个任务是问
# @Date: 14:46 2024/04/13

import gevent


def ask(name):
    print(f"{name}:我要买个手提包！")
    gevent.sleep(0)  # 模拟IO阻塞
    print(f"{name}:我想学个Python！")


def answer(name):
    print(f"{name}:买买买！")
    gevent.sleep(0)
    print(f"{name}:一定马上去学习！")


if __name__ == '__main__':
    a = gevent.spawn(ask, '小乔')  # 创建第一个协程
    b = gevent.spawn(answer, '周瑜')  # 创建第二个协程
    gevent.joinall([a, b])  # 自动切换并行切换
