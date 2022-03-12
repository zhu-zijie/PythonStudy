# 1.定位到最新电影
# 2.从该页面提取子页面的链接
# 3.请求子页面的链接地址，拿到下载的地址

import requests
import re
import csv

domain = "https://www.dydytt.net"
url = "https://www.dydytt.net/index2.htm"

resp = requests.get(url, verify=False)   #去掉安全验证
resp.encoding = resp.apparent_encoding
resp.close()

obj1 = re.compile(r"最新电影更新.*?<ul>(?P<a>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'>.*?</a><br/>", re.S)
obj3 = re.compile(r'<br />◎片　　名(?P<movie>.*?)<br />.*?<a target="_blank" href="(?P<movie_url>.*?)"><strong>', re.S)
result1 = obj1.finditer(resp.text)
main_href = []

# 找到提取子页面的链接
for it in result1:
    a = it.group('a')
    result2 = obj2.finditer(a)
    for itt in result2:
        href = domain+itt.group('href')
        main_href.append(href)

file = open("movie.csv", mode='w', encoding='gbk')
csvwriter = csv.writer(file)

# 删除列表第一个元素
main_href.pop(0)
for child_url in main_href:
    child_resp = requests.get(child_url)
    child_resp.encoding = child_resp.apparent_encoding
    result3 = obj3.finditer(child_resp.text)
    for result in result3:
        dict = result.groupdict()

        # dict = {"name": result3.group("name"), "url": result3.group("movie_url")}
        csvwriter.writerow(dict.values())
        print(result.group("movie")+"获取成功")
print("Over!!!")
child_resp.close()
file.close()







