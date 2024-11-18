# 多线程
from threading import Thread

# def func():
#     for i in range(1000):
#         print("func", i)
#
# if __name__ == '__main__':
#     t = Thread(target = func)# 创建线程并给线程安排任务
#     t.start()# 多线程状态为可以开始状态，具体执行时间由CPU决定
#     for i in range(1000):
#         print("main", i)

class MyThread(Thread):
    def run(self):
        for j in range(1000):
            print("子线程", j)

if __name__ == '__main__':
    t = MyThread()
    t.start()

    for i in range(1000):
        print("主线程", i)