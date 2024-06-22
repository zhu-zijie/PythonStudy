import time
from functools import wraps


def logger(func):
    @wraps(func)
    def write_logging(*args, **kwargs):
        print(f"[info] --time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        func(*args, **kwargs)

    return write_logging


@logger  # 使用装饰器来给所有的work增加记录日志的功能
def work():
    print("我在工作！")


@logger
def work_2(name1, name2):
    print(f"{name1}和{name2}在工作！")

work()
work_2("张三", "李四")
