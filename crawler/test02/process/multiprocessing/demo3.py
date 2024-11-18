# coding=utf-8
# @File: demo3.py
# @Author: zijier
# @Desc: 创建两个进程，一个负责读，一个负责写
# @Date: 16:13 2024/03/29

from multiprocessing import Process, Queue
import os
import time


# 负责写的进程
class WriteProcess(Process):
    def __init__(self, name, mq):
        Process.__init__(self)
        self.name = name
        self.mq = mq

    def run(self):
        # 把多条数据写入到队列中
        print(f"进程名字：{self.name}；已经启动：{os.getpid()}")
        for i in range(1, 6):
            # writer进程负责把数据写入Queue
            self.mq.put(i)
            time.sleep(1)
        print(f"进程名字：{self.name}；已经结束：{os.getpid()}")


# 负责读的进程
class ReadProcess(Process):
    def __init__(self, name, mq):
        Process.__init__(self)
        self.name = name
        self.mq = mq

    def run(self):
        print(f"进程名字：{self.name}；已经启动：{os.getpid()}")
        while True:
            # 当队列中没有数据，该行代码一直阻塞，get()是一个阻塞函数
            value = self.mq.get(True)
            print(value)


if __name__ == '__main__':
    queue = Queue()
    writeProcess = WriteProcess('writer', queue)
    readProcess = ReadProcess('reader', queue)

    # 启动两个进程
    writeProcess.start()
    readProcess.start()

    # 让父进程等待子进程结束
    writeProcess.join()
    # readProcess是一个死循环，readProcess.terminate()强制杀死进程
    readProcess.terminate()
    print("父进程结束！")
