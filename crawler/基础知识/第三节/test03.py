# requests.get同步操作-->异步操作aiohttp

import asyncio
import aiohttp

urls = {
    "http://i1.shaodiyejin.com/uploads/tu/201707/9999/42702c0cbd.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0311/ba002220c8c0d6dab4b6064e8d401b6e.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0311/1adc0d5ffcdf0acede03b016b36af9c1.jpg"
}


async def aiodownload(url):
    name = url.rsplit('/', 1)[1]  # 从右边切，切一次得到第一个
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # 写入文件
            with open("img/" + name, mode="wb") as file:  # 创建文件
                file.write(await resp.content.read())  # 读取内容是异步的，需要挂起
    print(name + "完成！")


async def main():
    task = []
    for url in urls:
        task.append(aiodownload(url))

    await asyncio.wait(task)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
