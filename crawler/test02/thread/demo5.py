# coding=utf-8
# @File: demo5.py
# @Author: zijier
# @Desc: 让每一个线程拥有一个独立的私有变量
# @Date: 21:58 2024/04/01
import random
import time
from threading import *


def run():
    local_var = local()
    local_var.numbers = [1]  # 每个线程先给一个初始值1
    time.sleep(random.random())
    for i in range(8):
        # 在私有变量中放入随机的数值
        local_var.numbers.append(random.choice(range(10)))
    print(current_thread(), local_var.numbers)


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = Thread(target=run)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print(current_thread())
