# coding=utf-8
# @File: demo2.py
# @Author: zijier
# @Desc: 
# @Date: 15:37 2024/03/29

from multiprocessing import Process
import os
import time


class MyProcess(Process):
    def __init__(self, name):
        Process.__init__(self)  # 加载父类提供给我们的功能
        self.name = name

    def run(self):  # 子进程在运行过程中执行的代码
        print('当前进程的ID:', os.getpid())  # 获取当前调用函数的进程ID
        print('父进程的ID:', os.getppid())  # 获取当前进程的父进程ID
        print('当前进程的名字:', self.name)

        time.sleep(3)


if __name__ == '__main__':
    start = time.time()
    # 创建十个子进程放入一个列表中
    process_list = []
    for i in range(10):
        p = MyProcess(f'process-{i + 1}')
        p.start()
        process_list.append(p)

    for p in process_list:
        # 一般需要父进程等待所有的子进程结束，才执行后面的代码，join等待当前的子进程p结束
        p.join()  # 十个子进程可以并行执行

    # 所有的子进程已经结束了
    time_range = time.time() - start
    print("十个子进程一共执行的时间是：", time_range)
