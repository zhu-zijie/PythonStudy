# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 
# @Date: 13:24 2024/04/13

import time
import threading
import random

event = threading.Event()  # 创建一个事件
event.set()  # 设置标志为真，门一开始就是打开的
status = 0  # 代表门的状态，如果0-3代表打开，如果等于3，代表关闭


def door():
    global status
    while True:
        print(f"当前门的状态为{status}")
        if status >= 3:
            print("门已经打开了三秒，需要自动关闭！")
            event.clear()
        if event.is_set():
            print("门已经打开了，可以通行了！")
        else:
            print("门已经关了，请用户自行刷卡！")
            event.wait()  # 门的线程阻塞等待
            continue
        time.sleep(1)
        status += 1  # status代表门开始的秒数


def person():
    global status
    n = 0
    while True:
        if event.is_set():
            n += 1
            print(f"门开着在，{n}号人进入门里面！")
        else:
            print(f"门关着，{n}号人刷卡之后，进入门里面！")
            event.set()  # 标志改为true
            status = 0
        time.sleep(random.randint(1, 10))


if __name__ == '__main__':
    d = threading.Thread(target=door)
    p = threading.Thread(target=person)
    d.start()
    p.start()
