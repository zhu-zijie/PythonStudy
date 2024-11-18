# coding=utf-8
# @File: demo4.py
# @Author: zijier
# @Desc: 所有子线程传入一个共同的参数，作为所有子线程的共享数据
# @Date: 21:52 2024/04/01

from threading import Thread
import time


def run1(num):
    for i in range(10):
        num[0] += 1
    print(f"线程1执行后的结果为{num[0]}")


def run2(num):
    print(f"线程1执行后的结果为{num[0]}")


if __name__ == '__main__':
    num = [0]
    t1 = Thread(target=run1, args=(num,))
    t2 = Thread(target=run2, args=(num,))
    t1.start()
    time.sleep(1)
    t2.start()
    print(f"最后的执行结果为{num[0]}")
