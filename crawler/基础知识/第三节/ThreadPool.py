from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# 一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度由线程池来完成

def fn(name):
    for i in range(100):
        print(name, i)

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name = f"线程{i}")
    print("Over!!!")



