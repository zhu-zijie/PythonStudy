# coding=utf-8
# @File: demo3.py
# @Author: zijier
# @Desc: 
# @Date: 15:01 2024/04/13
import asyncio


async def fun1():
    for i in range(5):
        print("协程a!!!")
        await asyncio.sleep(1)  # 人为的模拟IO阻塞


async def fun2():
    for i in range(5):
        print("协程b!!!")
        await asyncio.sleep(2)


# 获取循环事件
loop = asyncio.get_event_loop()

# 启动多个协程并行执行
loop.run_until_complete(asyncio.gather(fun1(), fun2()))

# 关闭事件
loop.close()
