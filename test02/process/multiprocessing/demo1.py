# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 
# @Date: 15:25 2024/03/29

from multiprocessing import Process
import os
import time


def funct1(name):
    print('当前进程的ID:', os.getpid())  # 获取当前调用函数的进程ID
    print('父进程的ID:', os.getppid())  # 获取当前进程的父进程ID
    print('当前进程的名字:', name)

    time.sleep(3)


if __name__ == '__main__':
    start = time.time()
    # 创建多个子进程，来调用funct1函数
    for i in range(10):
        p = Process(target=funct1, args=(f'进程{i}',))    # 创建一个子进程
        p.start()   # 开始子进程
