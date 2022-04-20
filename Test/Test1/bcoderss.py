'''
测试一下
https://m.bcoderss.com/
'''

import requests
import re
import os

def get_main_url(file):
    # 正则匹配出链接
    href = re.findall('<a target="_blank" href="(.*?)" alt="(.*?)" title="(.*?)">', file)
    return href

def download(url):
    resp = requests.get(url)
    title = url.split('/')[-1]
    with open('img/'+title, mode='wb') as f:
        f.write(resp.content)
    print("保存成功 "+title)

def get_url(url):
    kind = input("请输入下载的类型：")
    pages = int(input("请输入下载的页数："))
    for page in range(1, pages+1):
        url = f'{url}page/{page}/?s={kind}'

def get_file():
    path = 'img/'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)

def main(url):
    # 1.判断文件夹是否存在
    get_file()

    # 2.得到首页url
    get_url(url)
    # 3.获取到每个视频的url
    resp = requests.get(url)
    main_urls = get_main_url(resp.text)
    # print(main_url)
    for main_url in main_urls:
        page_url = main_url[0]
        # 4.获取图片页面url
        resp = requests.get(page_url)
        result = re.findall('<img alt="(.*?)" title="(.*?)" src="(.*?)">', resp.text)
        url = result[0][2]
        # print(url)
        # 5.下载图片
        download(url)

if __name__ == '__main__':
    url = 'https://m.bcoderss.com/'
    main(url)

