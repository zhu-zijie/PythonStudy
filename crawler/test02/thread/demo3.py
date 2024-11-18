# coding=utf-8
# @File: demo3.py
# @Author: zijier
# @Desc: 主线程中的全局变量，作为所有子线程的共享资源
# @Date: 21:43 2024/04/01

from threading import Thread
import time

num = 0


def run1():
    global num
    for i in range(10):
        num += 1
    print(f"线程1执行后的结果为{num}")


def run2():
    global num
    print(f"线程1执行后的结果为{num}")


if __name__ == '__main__':
    t1 = Thread(target=run1)
    t2 = Thread(target=run2)
    t1.start()
    time.sleep(1)
    t2.start()
    print(f"最后的执行结果为{num}")
