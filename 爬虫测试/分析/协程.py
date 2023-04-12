import asyncio

async def download(url):
    print("开始下载！")
    asyncio.sleep(3)
    print("下载结束！")

async def main():
    urls = [
        'https://www.baidu.com',
        'https://www.bilibili.com',
        'https://www.163.com'
    ]
    tasks = []
    for url in urls:
        func = asyncio.create_task(download(url))
        tasks.append(func)
    # tasks = [asyncio.create_task(download(url)) for url in urls]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
    