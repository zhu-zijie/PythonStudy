#拿到页面源代码
#提取和解析数据
import csv
import requests
from lxml import etree

# 拿到页面源代码
url = "https://beijing.zbj.com/logo/f.html"
resp = requests.get(url)

# print(resp.text)
# 解析
html = etree.HTML(resp.text)

divs = html.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")
file = open("logo.csv", mode='w', encoding='utf-8')
csvwriter = csv.writer(file)
for div in divs:
    company = div.xpath("./div/div/div[1]/div[1]/p/a/text()")[0]
    location = div.xpath("./div/div/div[1]/div[1]/div/span/text()")[0]
    price = div.xpath("./div/div/div[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    num = div.xpath("./div/div/div[2]/div[2]/div[1]/span[2]/text()")[0].split("：")[1]
    title = "LOGO".join(div.xpath("./div/div/div[2]/div[2]/div[2]/p/a/text()"))
    dict = {"title": title, "price": price, "company": company, "number": num, "location": location}
    csvwriter.writerow(dict.values())
print("Over!!!")
file.close()