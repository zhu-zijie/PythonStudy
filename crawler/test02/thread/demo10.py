# coding=utf-8
# @File: demo10.py
# @Author: zijier
# @Desc: 信号量：设置在多线程中，并行运行的线程个数
# @Date: 22:49 2024/04/07

from threading import *
import time

semapshore = BoundedSemaphore(3)  # 一次只运行同时三个人过安检


def run(num):
    semapshore.acquire()
    print(f"第{num}个人正在过安检！")
    time.sleep(5)
    semapshore.release()


if __name__ == '__main__':
    for i in range(100):
        thread = Thread(target=run, args=(i,))
        thread.start()
