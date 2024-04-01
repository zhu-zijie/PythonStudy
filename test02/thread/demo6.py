# coding=utf-8
# @File: demo6.py
# @Author: zijier
# @Desc: 线程共享数据混乱的问题
# @Date: 22:15 2024/04/01
from threading import *

num = 0


def run():
    print(f"当前的进程{current_thread()}，开始启动!")
    global num
    for i in range(5000000):
        num += 1
    print(f"线程{current_thread()}执行之后num的值为{num}")


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = Thread(target=run)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"主线程结束，num的值为{num}")
