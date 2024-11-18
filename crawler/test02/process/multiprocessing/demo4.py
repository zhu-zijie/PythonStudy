# coding=utf-8
# @File: demo3.py
# @Author: zijier
# @Desc: 创建两个进程，一个负责读，一个负责写
# @Date: 16:13 2024/03/29

from multiprocessing import Process, Pipe
import os
import time


# 负责写的进程
class WriteProcess(Process):
    def __init__(self, name, pipe):
        Process.__init__(self)
        self.name = name
        self.pipe = pipe

    def run(self):
        print(f"进程名字：{self.name}；已经启动：{os.getpid()}")
        for i in range(1, 6):
            # writer进程负责把数据通过管道发送给另一个进程
            self.pipe.send(i)
            time.sleep(1)
        print(f"进程名字：{self.name}；已经结束：{os.getpid()}")


# 负责读的进程
class ReadProcess(Process):
    def __init__(self, name, pipe):
        Process.__init__(self)
        self.name = name
        self.pipe = pipe

    def run(self):
        print(f"进程名字：{self.name}；已经启动：{os.getpid()}")
        while True:
            # 当管道中没有数据，该行代码一直阻塞，get()是一个阻塞函数
            value = self.pipe.recv()
            print(value)


if __name__ == '__main__':
    # Pipe创建之后得到管道的两端
    pipe1, pipe2 = Pipe()
    writeProcess = WriteProcess('writer', pipe1)
    readProcess = ReadProcess('reader', pipe2)

    # 启动两个进程
    writeProcess.start()
    readProcess.start()

    # 让父进程等待子进程结束
    writeProcess.join()
    # readProcess是一个死循环，readProcess.terminate()强制杀死进程
    readProcess.terminate()
    print("父进程结束！")
