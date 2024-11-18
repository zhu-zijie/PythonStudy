# coding=utf-8
# @File: demo8.py
# @Author: zijier
# @Desc: 死锁 Lock()是互斥锁，RLock()是逻辑锁
# @Date: 22:20 2024/04/07
import time
from threading import *

mutex_Yu = Lock()
mutex_XiongZhang = Lock()


class MyThread1(Thread):
    def run(self):
        mutex_Yu.acquire()  # 得到鱼
        print("线程1已经得到鱼！")
        time.sleep(1)

        mutex_XiongZhang.acquire()  # 得到熊掌
        print("线程1得到熊掌！")
        mutex_XiongZhang.release()
        mutex_Yu.release()


class MyThread2(Thread):
    def run(self):
        mutex_XiongZhang.acquire()  # 得到熊掌
        print("线程2已经得到熊掌！")
        time.sleep(1)

        mutex_Yu.acquire()  # 得到鱼
        print("线程2得到鱼！")
        mutex_Yu.release()
        mutex_XiongZhang.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
