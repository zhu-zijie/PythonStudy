import requests
from bs4 import BeautifulSoup
import time

# 这个链接只能下载第一页
url = "https://pic.netbian.com"

resp = requests.get(url)
resp.encoding = "gbk"#解决乱码问题
resp.close()

page = BeautifulSoup(resp.text, "html.parser")
lists = page.find("ul", attrs={"class": "clearfix"}).find_all("li")
for list in lists:
    page_url = url+list.find('a').get("href")
    #拿到子页面源代码
    child_page_resp = requests.get(page_url)
    child_page_resp.encoding = 'gbk'
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    page = child_page.find("div", attrs={"class": "photo-pic"})
    img = page.find("a", attrs={"id": "img"}).find("img")
    src = "https://pic.netbian.com"+img.get("src")
    name = img.get("title").split(' ')[0]
    #下载图片
    img_resp = requests.get(src)
    with open("img/"+name+".jpg", mode='wb') as file:
        file.write(img_resp.content)
    print("Over!", name)
    time.sleep(1)
print("Over!!!")
child_page_resp.close()
file.close()
