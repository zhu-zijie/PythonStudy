# coding=utf-8
# @File: demo2.py
# @Author: zijier
# @Desc: 使用类的封装来启动多线程
# @Date: 20:55 2024/04/01

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print(f"线程的名字{self.name}, 输出{i}")
            time.sleep(1)


if __name__ == '__main__':
    print(f"主线程开始的时间：{time.time()}")
    thread_list = []
    # 创建多个线程
    s = 'abcde'
    for i in range(5):
        t = MyThread(name=s[i])
        t.start()  # 启动线程
        thread_list.append(t)
    for j in thread_list:
        j.join()
    print("主线程结束！")
