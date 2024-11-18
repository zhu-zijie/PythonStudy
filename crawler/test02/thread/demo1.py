# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 使用函数启动多线程
# @Date: 20:41 2024/04/01

import threading
import time


def run(name):
    for i in range(3):
        print(f"线程的名字{name}, 输出{i}")
        time.sleep(1)


if __name__ == '__main__':
    print(f"主线程开始的时间：{time.time()}")

    # 创建多个线程
    s = 'abcde'
    for i in range(5):
        t = threading.Thread(target=run, name=s[i], args=(s[i],))
        t.start()  # 启动线程

    while True:
        count = len(threading.enumerate())  # 获取当前正在运行的线程数量
        print(f"当前正在执行的线程的数量为：{count}")
        if count <= 1:
            break

    print("主线程结束！")
