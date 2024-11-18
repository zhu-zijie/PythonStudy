import asyncio
import aiofiles
import aiohttp
import requests
import os

domain = 'https://h0.rzisytn.cn'

def download_m3u8(url):
    resp = requests.get(url)
    with open("data/m3u8.txt", mode='wb') as f:
        f.write(resp.content)

async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"data/video/{name}", mode='wb') as f:
            await f.write(await resp.content.read())
    print(f"{name}下载完毕！")

async def download_video():
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("data/m3u8.txt", mode='r', encoding='utf-8') as f:
            async for line in f:
                if line.startswith('#'):
                    continue
                else:
                    line = line.strip()
                    ts_url = domain + line
                    name = ts_url.rsplit('/', 1)[1]
                    task = asyncio.create_task(download_ts(ts_url, name, session))
                    tasks.append(task)
            await asyncio.wait(tasks)

def merge_ts():
    with open("data/movie.mp4", mode="wb") as file:
        with open("m3u8.txt", mode="r") as f1:
            for line in f1:
                if line.startswith("#"):
                    continue
                else:
                    file_name = line.rsplit("/", 1)[1]
                    with open("data/video/"+file_name, mode="rb") as f2:
                        content = f2.read()
                        file.write(content)
                    print(file_name+"合并成功")

    print("合并完成")

def main(url):
    # 1.下载m3u8文本文件
    download_m3u8(url)
    # 2.下载视频片段
    asyncio.run(download_video())
    # 3.合并视频
    merge_ts()

if __name__ == '__main__':
    url = "https://h0.rzisytn.cn/ppvod/6599C71BF3117CDA1E23771864C67EFD.m3u8"
    main(url)