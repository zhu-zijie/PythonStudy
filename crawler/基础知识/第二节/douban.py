import csv

import requests
import re

#请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

#解析数据
obj = re.compile(r'<div class="info">.*?<a href="(?P<url>.*?)" class="">.*?<span class="title">(?P<name>.*?)</span>.*?<div class="bd">.*?<p class="">.*?<br>(?P<year>.*?)'
                 r'&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;.*?<div class="star">.*?<span class="rating_num" property="v:average">(?P<score>.*?)'
                 r'</span>.*?<span>(?P<number>.*?)</span>', re.S)

for page in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={page}"
    # print(url)
    resp = requests.get(url, headers=header)
    #print(resp.text)
    page_content = resp.text
    # 开始匹配
    result = obj.finditer(page_content)
    file = open("data.csv", mode='a', encoding='utf-8', newline='')
    csvwriter = csv.writer(file)
    for it in result:
        # print(it.group("name"))
        # print(it.group("year").strip())
        # print(it.group("country"))
        # print(it.group("score"))
        # print(it.group("number"))
        # print(it.group("url"))
        dict = it.groupdict()
        dict['year'] = dict['year'].strip()
        csvwriter.writerow(dict.values())
    resp.close()
file.close()
print("Over!")