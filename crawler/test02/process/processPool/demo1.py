# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 
# @Date: 19:18 2024/03/29


from multiprocessing import Pool
import os
import time
import random


# 打印进程的信息，并记录该进程执行的时长
def run(name):
    start = time.time()
    print(f"进程名字：{name}；已经启动：{os.getpid()}")

    time.sleep(random.choice([1, 2, 3, 4, 5]))
    end = time.time()
    print(print(f"进程名字：{name}；已经结束：{os.getpid()}；耗时{end - start}"))


if __name__ == '__main__':
    pool = Pool(5)  # 默认为CPU的核心数
    for i in range(10):
        # 请求得到一个进程，然后异步调用run函数
        pool.apply_async(run, ('process' + str(i),))
    pool.close()
    pool.join()
    print("父进程结束！")
