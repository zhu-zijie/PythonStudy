'''
测速星辰影院  https://www.xcvods.com

1.从页面源代码直接拿到m3u8链接
2.下载第一层m3u8&下载第二层m3u8
3.下载视频
4.合并ts文件为一个mp4文件（此时视频不需要解密）

'''
import requests
import re
import aiohttp
import aiofiles
import asyncio
import os


def get_frist_m3u8(url):
    resp = requests.get(url)
    # print(resp.text)  #打印页面源代码
    obj = re.compile(r'"link_pre":"","url":"(?P<frist_m3u8>.*?)","url_next":""', re.S)
    frist_m3u8_url = obj.search(resp.text).group("frist_m3u8")    #从网页中拿到第一个m3u8链接
    return frist_m3u8_url

def download_m3u8(url, name):
    resp = requests.get(url)
    with open(name, mode='wb',) as f:
        f.write(resp.content)

async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}", mode="wb") as file:
            await file.write(await resp.content.read())
    print(f"{name}下载完毕！")

async def aio_download():
    tasks = []
    async with aiohttp.ClientSession() as session:  #提前准备好session
        async with aiofiles.open("送你一朵小红花_m3u8.txt", mode="r", encoding="utf-8") as file:
            async for line in file:
                if line.startswith("#"):
                    continue
                else:
                    # line就是xxx.ts， 去掉空格和换行
                    line.strip( )
                    # ts_url的链接
                    ts_url = line
                    name = ts_url.rsplit("/", 1)[1].strip( )
                    task = asyncio.create_task(download_ts(ts_url, name, session))
                    tasks.append(task)
            # 等待任务结束
            await asyncio.wait(tasks)

def merge_ts():
    list = []
    with open("送你一朵小红花_m3u8.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("#"):
                continue
            else:
                name = line.rsplit("/", 1)[1].strip( )
                list.append(name)
    s = ",".join(list)
    os.system(f"copy /b {s} movie.ts")
    print("搞定!")

def main(url):
    # 1.1从页面源代码直接拿到m3u8链接
    frist_m3u8_url = get_frist_m3u8(url)
    # 1.2把第一个m3u8的链接的\去掉
    frist_m3u8_url = frist_m3u8_url.replace("\\", "")

    # 2.下载第一层m3u8&下载第二层m3u8
    # download_m3u8(frist_m3u8_url, "送你一朵小红花.txt")
    # with open("送你一朵小红花.txt", mode="r", encoding="utf-8") as file:
    #     for line in file:
    #         if line.startswith('#'):
    #             continue
    #         else:
    #             line = line.strip()
    #             # 拼接第二层m3u8链接
    #             second_m3u8_url = "https://cdn.zoubuting.com"+line
    #             # 下载第二层m3u8
    #             download_m3u8(second_m3u8_url, "送你一朵小红花_m3u8.txt")

    # 3.下载视频
    #asyncio.run(aio_download())

    # 4.合并ts文件为一个mp4文件
    merge_ts()


if __name__ == '__main__':
    url = "https://www.xcvods.com/vod-play-id-63853-src-1-num-1.html"
    main(url)
