import requests
from bs4 import BeautifulSoup
import csv

url = f"https://www.cccsc.cn/"
resp = requests.get(url)
#print(resp.apparent_encoding)#打印当前编码格式
resp.encoding = resp.apparent_encoding
resp.close()

#解析数据
#1.把页面源代码交给BeautifulSoup进行处理，生产bs对象
page = BeautifulSoup(resp.text, "html.parser")  #指定html解析器

#2.从bs对象中查找数据
#find(标签, 属性=值）
#find_all(标签， 属性=值）
# title = page.find("div", class_ = "title")#class是关键字
title = page.find_all("div", attrs={"class": "content p-new"})[1:]
#写入文件
file = open("price.csv", mode='w', encoding='utf-8')
csvwriter = csv.writer(file)
for i in title:
    dl = i.find_all("dl")
    for j in dl:
        dd = j.find_all("dd")
        #print(dd[0].text, dd[1].text)
        dict = {"variety": dd[0].text, "price": dd[1].find("strong").text}
        csvwriter.writerow(dict.values())
file.close()
print("Over!")
