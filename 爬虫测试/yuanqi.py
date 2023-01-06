import requests
from lxml import etree
import threading
from queue import Queue
import os

pageUrlQueue = Queue()
downloadQueue = Queue()
dir_path = "picture/"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

def parsePageUrl(pages_start, pages):
    for page in range(pages_start, pages_start+pages):
        url = f"https://bizhi.ijinshan.com/dtag_109/index_{page}.shtml"
        print(url)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        }
        res = requests.get(url=url, headers=headers)
        res.encoding = res.apparent_encoding
        html = etree.HTML(res.text)

        divs = html.xpath("//div[@class='wallpaper-wrapper']/div")
        for div in divs:
            try:
                i = div.xpath("./a/@data-image-id")[0]
                d = div.xpath("./a/@data-classify-id")[0]
                u = "https://bizhi.ijinshan.com/d_" + d + "/" + i + ".shtml"
                pageUrlQueue.put(u)
            except:
                pass

def getDownloadUrl():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
    }
    while True:
        if not pageUrlQueue.empty():
            try:
                url = pageUrlQueue.get()
                res = requests.get(url=url, headers=headers)
                res.encoding = "utf-8"
                html = etree.HTML(res.text)
                src = html.xpath("/html/body/div[1]/section[1]/div[2]/div[1]/video/@src")[0]
                title = html.xpath("/html/body/div[1]/section[1]/div[1]/div/h1/text()")[0]
                downloadQueue.put((title, src))
            except:
                pass

def downloadDynamicWallPictrue():
    while True:
        if not downloadQueue.empty() and not pageUrlQueue.empty():
            title, src = downloadQueue.get()
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
            }
            res = requests.get(url=src, headers=headers).content
            with open(dir_path+"{}.mp4".format(title), "wb") as f:
                f.write(res)
            f.close()
            print(title, "下载成功")

def newThread(func, count):
    for _ in range(count):
        threading.Thread(target=func, ).start()


if __name__ == '__main__':
    pages_start = int(input("请输入开始爬取的页数："))
    pages = int(input("请输入爬取页数： "))
    parsePageUrl(pages_start,pages)

    newThread(getDownloadUrl, 5)
    newThread(downloadDynamicWallPictrue, 5)