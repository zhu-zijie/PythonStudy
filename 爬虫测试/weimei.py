import time

import aiohttp
import asyncio
import aiofiles

# urls = [
#     "https://img.vm.laomishuo.com/image/2021/04/2021040221005497.jpeg",
#     "https://img.vm.laomishuo.com/image/2021/04/2021040221005762.jpeg",
#     "https://img.vm.laomishuo.com/image/2021/04/2021040221005969.jpeg",
#     "https://img.vm.laomishuo.com/image/2021/04/2021040221010295.jpeg",
#     "https://img.vm.laomishuo.com/image/2021/04/2021040221010563.jpeg",
#     "https://img.vm.laomishuo.com/image/2021/04/2021040221010719.jpeg",
#     "https://img.vm.laomishuo.com/image/2021/04/2021040221011012.jpeg",
# ]
#
# async def aiodownload(url):
#     name = url.rsplit('/', 1)[1]
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             async with aiofiles.open("picture/"+name, mode='wb') as f:
#                 await f.write(await resp.content.read())
#     await asyncio.sleep(2)
#
# async def main():
#     tasks = []
#     for url in urls:
#         tasks.append(asyncio.create_task(aiodownload(url)))
#     await asyncio.wait(tasks)
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())

from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
import os

def download(title, url):
    name = url.rsplit('/', 1)[1]
    resp = requests.get(url)
    with open("picture/"+title+'/'+name, mode="wb") as f:
        f.write(resp.content)
    print(name+"    保存完毕！")


def child_parse_page(url):
    resp = requests.get(url)
    tree = etree.HTML(resp.text)
    title = tree.xpath("/html/body/main/div/div[2]/div[1]/div/div/h1/text()")[0]
    file_dir = "picture/" + title
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    pics = tree.xpath("/html/body/main/div/div[2]/div[1]/div/div/div[3]/div[1]/p")
    for pic in pics:
        pic_url = pic.xpath("./a/@href")[0]
        download(title, str(pic_url))

def main_parse_page(page):
    url = f"https://www.vmgirls.net/page/{page}"
    resp = requests.get(url)
    tree = etree.HTML(resp.text)
    lis = tree.xpath("/html/body/div[3]/div/div/div")
    with ThreadPoolExecutor(6) as t:
        for li in lis:
            href = li.xpath("./div/div[1]/a/@href")[0]
            t.submit(child_parse_page, href)

def main():
    pages = int(input("请输入要下载的页数："))
    for page in range(1, pages+1):
        main_parse_page(page)

if __name__ == '__main__':
    main()


