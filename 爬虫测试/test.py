import requests
import re
import csv
import time
from bs4 import BeautifulSoup

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
# 案例1
# from urllib.request import urlopen
# url = "http://www.baidu.com"
#
# resp = urlopen(url)
# print(resp.read().decode('utf-8'))

# 案例2
# url = 'https://fanyi.baidu.com/sug'
# input = input("请输入你要查询的单词：")
# data = {
#     'kw': input
# }
# resp = requests.post(url, data=data)
#
# print(resp.json())

# 案例3
# url = "https://movie.douban.com/top250"

#
# resp = requests.get(url, headers=headers)
# print(resp.text)

# 案例4
# url = "https://movie.douban.com/j/chart/top_list"
#
# params = {
#     'type': 24,
#     'interval_id': '100:90',
#     'action': '',
#     'start': 0,
#     'limit': 20
# }
# resp = requests.get(url, params=params, headers=headers)
# # print(resp.request.url)
# print(resp.json())
# resp.close()

# 案例5
# 爬取豆瓣前250的电影----稍微有点问题，有15部电影没有匹配到（如釜山行，应该是正则匹配出现问题）
# file = open("data.csv", mode='w', encoding="utf-8", newline="")
# csvwriter = csv.writer(file)
# for page in range(0,250,25):
#     url = f"https://movie.douban.com/top250?start={page}"
#     # 获取数据
#     resp = requests.get(url, headers=headers)
#     # print(resp.text)
#     page_content = resp.text
#     # 解析数据
#     obj = re.compile(
#         r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;'
#         r'(?P<type>.*?)</p>.*? <span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?</span>.*?'
#         r'<span>(?P<number>.*?)人评价</span>.*?<span class="inq">(?P<quoto>.*?)</span>', re.S)
#     results = obj.finditer(page_content)
#
#     for result in results:
#         # print(result.group("name"))
#         # print(result.group("year").strip())
#         # print(result.group("country"))
#         # print(result.group("type").strip())
#         # print(result.group("score"))
#         # print(result.group("number").strip())
#         # print(result.group("quoto"))
#         dic = result.groupdict()
#         dic["year"] = dic["year"].strip()
#         dic["type"] = dic["type"].strip()
#         dic["number"] = dic["number"].strip()
#         csvwriter.writerow(dic.values())
# resp.close()
# file.close()
# print("Over!")

# 案例6
# 爬取电影天堂
# domain = "https://www.dytt89.com"   # 域名，待会下载使用
# # 获取数据
# main_resp = requests.get(domain)
# main_resp.encoding = "gbk"  # 编码为gbk
# # print(main_resp.text)
#
# # 解析数据
# main_obj = re.compile(r"2023必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
# ul = main_obj.search(main_resp.text)
# ul = ul.group("ul").strip()     # 获取ul
#
# # 从ul中获取li
# ul_obj = re.compile(r"<li><a href='(.*?)'", re.S)
# lis = ul_obj.findall(ul)
# li_obj = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?◎主　　演　(?P<actors>.*?)<br />◎简　　介<br />(?P<brief_introduction>.*?)'
#                      r'<br />.*?<td style="WORD-WRAP:.*?href="(?P<download>.*?)">', re.S)
# # 写入到文件中
# file = open('movie.csv', mode='w', encoding='utf-8', newline='')
# csvwriter = csv.writer(file)
#
# for li in lis:
#     url = domain+li     # 拼接成子页面的url
#     resp = requests.get(url)
#     resp.encoding = "gbk"
#     # movie = li_obj.search(resp.text).group("movie")
#     # actors = li_obj.search(resp.text).group("actors").replace("<br />　　　　　　", "&").replace("&middot;", "_")
#     # brief_introduction = li_obj.search(resp.text).group("brief_introduction").strip().strip("&hellip;").strip("&rdquo;")
#     # download = li_obj.search(resp.text).group("download")
#     # print(movie, actors, brief_introduction, download)
#     li = li_obj.search(resp.text)
#     dic = li.groupdict()
#     dic["actors"] = li_obj.search(resp.text).group("actors").replace("<br />　　　　　　", "&").replace("&middot;", "_")
#     dic["brief_introduction"] = li_obj.search(resp.text).group("brief_introduction").strip().strip("&hellip;").strip("&rdquo;").strip("&ldquo;")
#     csvwriter.writerow(dic.values())
#
# file.close()
# main_resp.close()
# resp.close()
# print("Over!")

# 案例7
# 爬取唯美图片
# domain = "https://www.youmeitu.com"
# url = "https://www.youmeitu.com/weimeitupian/"
# headers = {
#     "referer": "https://www.youmeitu.com/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
#
# resp = requests.get(url, headers=headers)
# # print(resp.text)
#
# # 解析数据
# main_page = BeautifulSoup(resp.text, "html.parser")
# lis = main_page.find("div", attrs={"class": "TypeList"}).find_all("a", attrs={"class": "TypeBigPics"})
# for li in lis:
#     href = li.get("href")
#     url = domain+href
#     child_resp = requests.get(url)
#     child_page = BeautifulSoup(child_resp.text, "html.parser")
#     src = domain+child_page.find("div", attrs={"class": "ImageBody"}).find("img").get("src")
#     img_resp = requests.get(src)
#     img_name = src.split("/")[-1]
#     # print(img_name)
#     with open("picture/"+img_name, mode="wb") as file:
#         file.write(img_resp.content)
#         print("Over!", img_name)
#
# img_resp.close()
# child_resp.close()
# resp.close()
# print("当前页已经下载完毕！")
