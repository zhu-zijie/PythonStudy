# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 线程通信
# @Date: 23:03 2024/04/07

import threading
import time
import queue

# 创建一个队列
q = queue.Queue(1000)  # 先进先出的队列，1000代表maxSize


# q = queue.LifoQueue  # 先进后出的队列
# q = queue.PriorityQueue  # 优先级的队列


# 定义生产者线程
class Producer(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = f"产品{count}"
                    q.put(msg)
                    print(msg)
            time.sleep(2)


# 定义消费者线程
class Consumer(threading.Thread):
    def run(self):
        global q
        while True:
            for i in range(100):
                msg = q.get()
                print(f"消费者得到了数据：{msg}")
            time.sleep(3)


if __name__ == '__main__':
    p1 = Producer()

    c1 = Consumer()
    p1.start()
    c1.start()
