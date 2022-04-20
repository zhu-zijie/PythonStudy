#1.拿到主页面的源代码，然后提取到子页面的链接地址：href
#2.通过href拿到子页面的内容，从子页面中找到图片的下载地址
#3.下载图片

import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umeitu.com/bizhitupian/xiaoqingxinbizhi/"

resp = requests.get(url)
resp.encoding = "urf-8"#解决编码问题

#print(resp.text)
#把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
list = main_page.find("div", attrs={"class": "TypeList"}).find_all('a')
for a in list:
    href = a.get('href')    #直接通过get拿到属性的值
    page_url = "https://www.umeitu.com"+href
    #print(page_url)
    #拿到子页面源代码
    child_page_resp = requests.get(page_url)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    #从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    page = child_page.find("div", attrs={"class": "ImageBody"})
    img = page.find("img")
    src = img.get('src')
    #下载图片
    img_resp = requests.get(src)    #img_resp.content拿到的是字节
    img_name = src.split("/")[-1]   #拿到url最后一个/的内容
    with open("img/"+img_name, mode='wb') as file:
        file.write(img_resp.content)
    print("Over!", img_name)
    time.sleep(1)
print("Over!!!")


